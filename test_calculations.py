#!/usr/bin/env python3
"""
Test script for calculations.py module
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from calculations import (
    CalculationUtils,
    UnitConverter,
    DataValidator,
    MetricsCalculator,
    DataFormatter,
    normalize_storage,
    normalize_time
)

def test_unit_converter():
    """Test unit conversion functions."""
    print("=" * 60)
    print("Testing UnitConverter")
    print("=" * 60)
    
    # Test storage conversion
    try:
        tb_to_gb = UnitConverter.convert_storage(1, 'TB', 'GB')
        assert abs(tb_to_gb - 1024) < 0.01
        print(f"✓ 1 TB = {tb_to_gb} GB")
    except Exception as e:
        print(f"✗ Storage conversion failed: {e}")
    
    try:
        gb_to_tb = UnitConverter.convert_storage(500, 'GB', 'TB')
        assert abs(gb_to_tb - 0.49) < 0.01
        print(f"✓ 500 GB = {gb_to_tb:.2f} TB")
    except Exception as e:
        print(f"✗ Storage conversion failed: {e}")
    
    # Test time conversion
    try:
        h_to_min = UnitConverter.convert_time(2, 'h', 'm')
        assert abs(h_to_min - 120) < 0.01
        print(f"✓ 2 hours = {h_to_min} minutes")
    except Exception as e:
        print(f"✗ Time conversion failed: {e}")
    
    # Test storage parsing
    try:
        result = UnitConverter.parse_storage_string("1.5 TB")
        assert result.is_valid
        assert result.value == 1.5
        assert result.unit == 'TB'
        print(f"✓ Parsed '1.5 TB': {result.value} {result.unit}")
    except Exception as e:
        print(f"✗ Storage parsing failed: {e}")
    
    # Test time parsing
    try:
        result = UnitConverter.parse_time_string("5 minutes")
        assert result.is_valid
        assert result.value == 5
        assert result.unit == 'm'
        print(f"✓ Parsed '5 minutes': {result.value} {result.unit}")
    except Exception as e:
        print(f"✗ Time parsing failed: {e}")
    
    print()

def test_data_validator():
    """Test data validation functions."""
    print("=" * 60)
    print("Testing DataValidator")
    print("=" * 60)
    
    # Test numeric validation
    try:
        result = DataValidator.validate_numeric_value("150", min_val=0, max_val=1000)
        assert result.is_valid
        print(f"✓ Validated numeric value: {result.value}")
    except Exception as e:
        print(f"✗ Numeric validation failed: {e}")
    
    # Test storage capacity validation
    try:
        result = DataValidator.validate_storage_capacity("1.5 TB")
        assert result.is_valid
        print(f"✓ Validated storage capacity: {result.value} {result.unit}")
    except Exception as e:
        print(f"✗ Storage validation failed: {e}")
    
    # Test VM count validation
    try:
        result = DataValidator.validate_vm_count("3500")
        assert result.is_valid
        print(f"✓ Validated VM count: {result.value} {result.unit}")
    except Exception as e:
        print(f"✗ VM count validation failed: {e}")
    
    print()

def test_metrics_calculator():
    """Test metrics calculation functions."""
    print("=" * 60)
    print("Testing MetricsCalculator")
    print("=" * 60)
    
    # Test data transfer time calculation
    try:
        result = MetricsCalculator.calculate_data_transfer_time(100, 1000)
        assert 'hours' in result
        print(f"✓ Transfer time for 100 GB at 1000 Mbps:")
        print(f"  - {result['hours']:.2f} hours")
        print(f"  - {result['minutes']:.2f} minutes")
    except Exception as e:
        print(f"✗ Transfer time calculation failed: {e}")
    
    # Test storage efficiency calculation
    try:
        efficiency = MetricsCalculator.calculate_storage_efficiency(80, 100)
        assert abs(efficiency - 80.0) < 0.01
        print(f"✓ Storage efficiency: {efficiency}%")
    except Exception as e:
        print(f"✗ Storage efficiency calculation failed: {e}")
    
    # Test cost savings calculation
    try:
        savings = MetricsCalculator.calculate_cost_savings(100000, 60000)
        assert savings['percentage'] == 40.0
        print(f"✓ Cost savings: {savings['absolute']} ({savings['percentage']}%)")
    except Exception as e:
        print(f"✗ Cost savings calculation failed: {e}")
    
    print()

def test_data_formatter():
    """Test data formatting functions."""
    print("=" * 60)
    print("Testing DataFormatter")
    print("=" * 60)
    
    # Test storage formatting
    try:
        formatted = DataFormatter.format_storage(1.5, 'TB')
        assert formatted == "1.5 TB"
        print(f"✓ Formatted storage: {formatted}")
    except Exception as e:
        print(f"✗ Storage formatting failed: {e}")
    
    # Test time formatting
    try:
        formatted = DataFormatter.format_time(120, 'minutes')
        assert formatted == "120.0 minutes"
        print(f"✓ Formatted time: {formatted}")
    except Exception as e:
        print(f"✗ Time formatting failed: {e}")
    
    # Test percentage formatting
    try:
        formatted = DataFormatter.format_percentage(85.67)
        assert formatted == "85.7%"
        print(f"✓ Formatted percentage: {formatted}")
    except Exception as e:
        print(f"✗ Percentage formatting failed: {e}")
    
    # Test VM count formatting
    try:
        formatted = DataFormatter.format_vm_count(3500)
        assert formatted == "3500+ VMs"
        print(f"✓ Formatted VM count: {formatted}")
    except Exception as e:
        print(f"✗ VM count formatting failed: {e}")
    
    print()

def test_calculation_utils():
    """Test CalculationUtils main interface."""
    print("=" * 60)
    print("Testing CalculationUtils (Main Interface)")
    print("=" * 60)
    
    utils = CalculationUtils()
    
    # Test storage extraction and normalization
    try:
        normalized = utils.extract_and_normalize_storage("500 GB", "TB")
        assert "TB" in normalized
        print(f"✓ Normalized storage '500 GB' to: {normalized}")
    except Exception as e:
        print(f"✗ Storage normalization failed: {e}")
    
    # Test time extraction and normalization
    try:
        normalized = utils.extract_and_normalize_time("2 hours", "minutes")
        assert "minutes" in normalized
        print(f"✓ Normalized time '2 hours' to: {normalized}")
    except Exception as e:
        print(f"✗ Time normalization failed: {e}")
    
    # Test metrics calculation from project data
    try:
        project_data = {
            'scale': '3500+ VMs, 存储约 1.5 TB',
            'customer': 'Test Customer'
        }
        metrics = utils.calculate_metrics(project_data)
        assert 'storage_normalized' in metrics
        assert 'vm_count_formatted' in metrics
        print(f"✓ Calculated metrics:")
        print(f"  - Storage: {metrics.get('storage_normalized')}")
        print(f"  - VMs: {metrics.get('vm_count_formatted')}")
    except Exception as e:
        print(f"✗ Metrics calculation failed: {e}")
    
    print()

def test_convenience_functions():
    """Test convenience functions."""
    print("=" * 60)
    print("Testing Convenience Functions")
    print("=" * 60)
    
    # Test normalize_storage
    try:
        normalized = normalize_storage("1000 GB")
        assert "TB" in normalized
        print(f"✓ normalize_storage('1000 GB'): {normalized}")
    except Exception as e:
        print(f"✗ normalize_storage failed: {e}")
    
    # Test normalize_time
    try:
        normalized = normalize_time("3 hours")
        assert "minutes" in normalized
        print(f"✓ normalize_time('3 hours'): {normalized}")
    except Exception as e:
        print(f"✗ normalize_time failed: {e}")
    
    print()

def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("CALCULATION MODULE TEST SUITE")
    print("=" * 60 + "\n")
    
    test_unit_converter()
    test_data_validator()
    test_metrics_calculator()
    test_data_formatter()
    test_calculation_utils()
    test_convenience_functions()
    
    print("=" * 60)
    print("TEST SUITE COMPLETED")
    print("=" * 60)

if __name__ == '__main__':
    run_all_tests()