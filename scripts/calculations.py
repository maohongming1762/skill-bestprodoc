#!/usr/bin/env python3
"""
HyperBDR Best Practices - Calculation Utilities

This module provides calculation utilities for ensuring accuracy in
best practices documentation generation, including unit conversions,
data validation, and metrics calculations.
"""

import re
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass


@dataclass
class CalculationResult:
    """Result of a calculation with metadata."""
    value: Union[int, float, str]
    unit: str
    original: str
    is_valid: bool
    error: Optional[str] = None


class UnitConverter:
    """Handle unit conversions for storage, time, and bandwidth."""
    
    STORAGE_UNITS = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4,
        'PB': 1024 ** 5
    }
    
    TIME_UNITS = {
        's': 1,
        'm': 60,
        'h': 3600,
        'd': 86400
    }
    
    BANDWIDTH_UNITS = {
        'bps': 1,
        'Kbps': 1000,
        'Mbps': 1000 ** 2,
        'Gbps': 1000 ** 3
    }
    
    @staticmethod
    def convert_storage(value: float, from_unit: str, to_unit: str) -> float:
        """Convert storage value between units (B, KB, MB, GB, TB, PB)."""
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        if from_unit not in UnitConverter.STORAGE_UNITS:
            raise ValueError(f"Unknown storage unit: {from_unit}")
        if to_unit not in UnitConverter.STORAGE_UNITS:
            raise ValueError(f"Unknown storage unit: {to_unit}")
        
        # Convert to bytes first, then to target unit
        bytes_value = value * UnitConverter.STORAGE_UNITS[from_unit]
        return bytes_value / UnitConverter.STORAGE_UNITS[to_unit]
    
    @staticmethod
    def convert_time(value: float, from_unit: str, to_unit: str) -> float:
        """Convert time value between units (s, m, h, d)."""
        if from_unit not in UnitConverter.TIME_UNITS:
            raise ValueError(f"Unknown time unit: {from_unit}")
        if to_unit not in UnitConverter.TIME_UNITS:
            raise ValueError(f"Unknown time unit: {to_unit}")
        
        # Convert to seconds first, then to target unit
        seconds_value = value * UnitConverter.TIME_UNITS[from_unit]
        return seconds_value / UnitConverter.TIME_UNITS[to_unit]
    
    @staticmethod
    def convert_bandwidth(value: float, from_unit: str, to_unit: str) -> float:
        """Convert bandwidth value between units (bps, Kbps, Mbps, Gbps)."""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in UnitConverter.BANDWIDTH_UNITS:
            raise ValueError(f"Unknown bandwidth unit: {from_unit}")
        if to_unit not in UnitConverter.BANDWIDTH_UNITS:
            raise ValueError(f"Unknown bandwidth unit: {to_unit}")
        
        # Convert to bps first, then to target unit
        bps_value = value * UnitConverter.BANDWIDTH_UNITS[from_unit]
        return bps_value / UnitConverter.BANDWIDTH_UNITS[to_unit]
    
    @staticmethod
    def parse_storage_string(text: str) -> CalculationResult:
        """Parse storage string like '1.5 TB' or '500 GB' into value and unit."""
        pattern = r'(\d+\.?\d*)\s*([KMGT]?B)'
        match = re.search(pattern, text, re.IGNORECASE)
        
        if not match:
            return CalculationResult(
                value=0,
                unit='GB',
                original=text,
                is_valid=False,
                error=f"Could not parse storage value from: {text}"
            )
        
        value = float(match.group(1))
        unit = match.group(2).upper()
        
        return CalculationResult(
            value=value,
            unit=unit,
            original=text,
            is_valid=True
        )
    
    @staticmethod
    def parse_time_string(text: str) -> CalculationResult:
        """Parse time string like '5 minutes' or '2h' into value and unit."""
        patterns = [
            r'(\d+\.?\d*)\s*(seconds?|s)',
            r'(\d+\.?\d*)\s*(minutes?|m)',
            r'(\d+\.?\d*)\s*(hours?|h)',
            r'(\d+\.?\d*)\s*(days?|d)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                value = float(match.group(1))
                unit_text = match.group(2).lower()
                unit = unit_text[0]  # First character (s, m, h, d)
                
                return CalculationResult(
                    value=value,
                    unit=unit,
                    original=text,
                    is_valid=True
                )
        
        return CalculationResult(
            value=0,
            unit='m',
            original=text,
            is_valid=False,
            error=f"Could not parse time value from: {text}"
        )


class DataValidator:
    """Validate data extracted from project data."""
    
    @staticmethod
    def validate_numeric_value(
        value: Union[int, float, str],
        min_val: Optional[float] = None,
        max_val: Optional[float] = None
    ) -> CalculationResult:
        """Validate a numeric value against min/max constraints."""
        try:
            if isinstance(value, str):
                # Extract first number from string
                match = re.search(r'-?\d+\.?\d*', value)
                if not match:
                    return CalculationResult(
                        value=0,
                        unit='',
                        original=str(value),
                        is_valid=False,
                        error=f"No numeric value found in: {value}"
                    )
                value = float(match.group(0))
            
            value = float(value)
            
            if min_val is not None and value < min_val:
                return CalculationResult(
                    value=value,
                    unit='',
                    original=str(value),
                    is_valid=False,
                    error=f"Value {value} is below minimum {min_val}"
                )
            
            if max_val is not None and value > max_val:
                return CalculationResult(
                    value=value,
                    unit='',
                    original=str(value),
                    is_valid=False,
                    error=f"Value {value} exceeds maximum {max_val}"
                )
            
            return CalculationResult(
                value=value,
                unit='',
                original=str(value),
                is_valid=True
            )
            
        except (ValueError, TypeError) as e:
            return CalculationResult(
                value=0,
                unit='',
                original=str(value),
                is_valid=False,
                error=f"Invalid numeric value: {e}"
            )
    
    @staticmethod
    def validate_storage_capacity(text: str) -> CalculationResult:
        """Validate and normalize storage capacity."""
        result = UnitConverter.parse_storage_string(text)
        
        if not result.is_valid:
            return result
        
        # Validate reasonable range (0 to 100 PB)
        if isinstance(result.value, (int, float)) and result.value > 100:
            return CalculationResult(
                value=result.value,
                unit=result.unit,
                original=text,
                is_valid=False,
                error=f"Storage capacity {result.value} {result.unit} exceeds reasonable limit"
            )
        
        return result
    
    @staticmethod
    def validate_rpo_rto(text: str) -> CalculationResult:
        """Validate RPO/RTO time values."""
        result = UnitConverter.parse_time_string(text)
        
        if not result.is_valid:
            return result
        
        # Validate reasonable range (0 to 30 days)
        if isinstance(result.value, (int, float)) and result.value > 30:
            return CalculationResult(
                value=result.value,
                unit=result.unit,
                original=text,
                is_valid=False,
                error=f"Time value {result.value} {result.unit} exceeds reasonable limit"
            )
        
        return result
    
    @staticmethod
    def validate_vm_count(text: str) -> CalculationResult:
        """Validate VM count."""
        result = DataValidator.validate_numeric_value(text, min_val=0, max_val=100000)
        
        if result.is_valid:
            result.unit = 'VMs'
        
        return result


class MetricsCalculator:
    """Calculate metrics for best practices documentation."""
    
    @staticmethod
    def calculate_data_transfer_time(
        size_gb: float,
        bandwidth_mbps: float,
        compression_ratio: float = 1.0
    ) -> Dict[str, float]:
        """
        Calculate data transfer time.
        
        Args:
            size_gb: Data size in GB
            bandwidth_mbps: Bandwidth in Mbps
            compression_ratio: Compression ratio (e.g., 0.7 for 30% compression)
        
        Returns:
            Dictionary with time in different units
        """
        if bandwidth_mbps <= 0:
            raise ValueError("Bandwidth must be positive")
        
        # Convert GB to Mb
        size_mb = size_gb * 1024 * 8
        
        # Apply compression
        effective_size_mb = size_mb * compression_ratio
        
        # Calculate time in seconds
        time_seconds = effective_size_mb / bandwidth_mbps
        
        return {
            'seconds': time_seconds,
            'minutes': time_seconds / 60,
            'hours': time_seconds / 3600,
            'days': time_seconds / 86400
        }
    
    @staticmethod
    def calculate_storage_efficiency(used_tb: float, total_tb: float) -> float:
        """Calculate storage efficiency as percentage."""
        if total_tb <= 0:
            raise ValueError("Total storage must be positive")
        
        efficiency = (used_tb / total_tb) * 100
        return round(efficiency, 2)
    
    @staticmethod
    def calculate_rpo_achievable(
        sync_interval_seconds: float,
        network_latency_seconds: float
    ) -> bool:
        """
        Determine if RPO is achievable.
        
        Returns True if sync interval is reasonable given network latency.
        """
        # RPO is achievable if sync interval is at least 10x network latency
        return sync_interval_seconds >= (network_latency_seconds * 10)
    
    @staticmethod
    def calculate_cost_savings(
        traditional_cost: float,
        hyperbdr_cost: float
    ) -> Dict[str, float]:
        """
        Calculate cost savings.
        
        Returns:
            Dictionary with absolute and percentage savings
        """
        if traditional_cost <= 0:
            raise ValueError("Traditional cost must be positive")
        
        absolute_savings = traditional_cost - hyperbdr_cost
        percentage_savings = (absolute_savings / traditional_cost) * 100
        
        return {
            'absolute': round(absolute_savings, 2),
            'percentage': round(percentage_savings, 2)
        }
    
    @staticmethod
    def calculate_bandwidth_utilization(
        actual_mbps: float,
        available_mbps: float
    ) -> float:
        """Calculate bandwidth utilization as percentage."""
        if available_mbps <= 0:
            raise ValueError("Available bandwidth must be positive")
        
        utilization = (actual_mbps / available_mbps) * 100
        return round(utilization, 2)


class DataFormatter:
    """Format calculated values for display."""
    
    @staticmethod
    def format_storage(value: float, target_unit: str = 'TB', precision: int = 2) -> str:
        """Format storage value with unit."""
        return f"{round(value, precision)} {target_unit}"
    
    @staticmethod
    def format_time(value: float, target_unit: str = 'minutes', precision: int = 2) -> str:
        """Format time value with unit."""
        return f"{round(value, precision)} {target_unit}"
    
    @staticmethod
    def format_bandwidth(value: float, target_unit: str = 'Mbps', precision: int = 2) -> str:
        """Format bandwidth value with unit."""
        return f"{round(value, precision)} {target_unit}"
    
    @staticmethod
    def format_percentage(value: float, precision: int = 1) -> str:
        """Format percentage value."""
        return f"{round(value, precision)}%"
    
    @staticmethod
    def format_vm_count(count: int) -> str:
        """Format VM count with plus sign if needed."""
        return f"{count}+ VMs" if count >= 1000 else f"{count} VMs"


class CalculationUtils:
    """Main utility class combining all calculation functions."""
    
    def __init__(self):
        self.converter = UnitConverter()
        self.validator = DataValidator()
        self.calculator = MetricsCalculator()
        self.formatter = DataFormatter()
    
    def extract_and_normalize_storage(self, text: str, target_unit: str = 'TB') -> str:
        """
        Extract storage value from text and normalize to target unit.
        
        Args:
            text: Text containing storage value (e.g., '1.5 TB', '500 GB')
            target_unit: Target unit for normalization (default: TB)
        
        Returns:
            Formatted string with normalized value
        """
        # Parse storage value
        result = self.validator.validate_storage_capacity(text)
        
        if not result.is_valid:
            # Return original text if parsing fails
            return text
        
        try:
            # Convert to target unit
            normalized_value = UnitConverter.convert_storage(
                float(result.value),
                result.unit,
                target_unit
            )
            
            # Format result
            return self.formatter.format_storage(normalized_value, target_unit)
            
        except Exception as e:
            # Return original text if conversion fails
            return text
    
    def extract_and_normalize_time(self, text: str, target_unit: str = 'minutes') -> str:
        """
        Extract time value from text and normalize to target unit.
        
        Args:
            text: Text containing time value (e.g., '5 minutes', '2h')
            target_unit: Target unit for normalization (default: minutes)
        
        Returns:
            Formatted string with normalized value
        """
        # Parse time value
        result = self.validator.validate_rpo_rto(text)
        
        if not result.is_valid:
            # Return original text if parsing fails
            return text
        
        try:
            # Convert to target unit
            normalized_value = UnitConverter.convert_time(
                float(result.value),
                result.unit,
                target_unit[0]  # Use first character
            )
            
            # Format result
            return self.formatter.format_time(normalized_value, target_unit)
            
        except Exception as e:
            # Return original text if conversion fails
            return text
    
    def calculate_metrics(self, project_data: Dict) -> Dict[str, str]:
        """
        Calculate key metrics from project data.
        
        Args:
            project_data: Dictionary containing project information
        
        Returns:
            Dictionary with calculated metrics
        """
        metrics = {}
        
        # Extract and normalize storage
        if 'scale' in project_data:
            metrics['storage_normalized'] = self.extract_and_normalize_storage(
                project_data['scale']
            )
        
        # Extract VM count
        if 'scale' in project_data:
            vm_match = re.search(r'(\d+)\s*\+', project_data['scale'])
            if vm_match:
                vm_count = int(vm_match.group(1))
                metrics['vm_count_formatted'] = self.formatter.format_vm_count(vm_count)
        
        return metrics


# Convenience functions for backward compatibility
def normalize_storage(text: str, target_unit: str = 'TB') -> str:
    """Normalize storage value to target unit."""
    utils = CalculationUtils()
    return utils.extract_and_normalize_storage(text, target_unit)


def normalize_time(text: str, target_unit: str = 'minutes') -> str:
    """Normalize time value to target unit."""
    utils = CalculationUtils()
    return utils.extract_and_normalize_time(text, target_unit)


def calculate_transfer_time(size_gb: float, bandwidth_mbps: float) -> Dict[str, float]:
    """Calculate data transfer time."""
    return MetricsCalculator.calculate_data_transfer_time(size_gb, bandwidth_mbps)


def format_percentage(value: float) -> str:
    """Format percentage value."""
    return DataFormatter.format_percentage(value)