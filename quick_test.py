#!/usr/bin/env python3
"""
Simple test to verify calculations module works
"""

import sys
sys.path.insert(0, 'scripts')

try:
    from calculations import CalculationUtils, UnitConverter, DataFormatter
    print("✓ Successfully imported calculations module")
except Exception as e:
    print(f"✗ Failed to import calculations module: {e}")
    sys.exit(1)

# Test 1: Unit conversion
try:
    result = UnitConverter.convert_storage(1, 'TB', 'GB')
    assert abs(result - 1024) < 0.01
    print(f"✓ Test 1 PASSED: UnitConverter.convert_storage(1 TB, GB) = {result} GB")
except Exception as e:
    print(f"✗ Test 1 FAILED: {e}")
    sys.exit(1)

# Test 2: Storage parsing
try:
    result = UnitConverter.parse_storage_string("1.5 TB")
    assert result.is_valid
    assert result.value == 1.5
    print(f"✓ Test 2 PASSED: UnitConverter.parse_storage_string('1.5 TB') = {result.value} {result.unit}")
except Exception as e:
    print(f"✗ Test 2 FAILED: {e}")
    sys.exit(1)

# Test 3: Storage normalization
try:
    utils = CalculationUtils()
    result = utils.extract_and_normalize_storage("500 GB", "TB")
    print(f"✓ Test 3 PASSED: CalculationUtils.extract_and_normalize_storage('500 GB', 'TB') = {result}")
except Exception as e:
    print(f"✗ Test 3 FAILED: {e}")
    sys.exit(1)

# Test 4: Time normalization
try:
    result = utils.extract_and_normalize_time("2 hours", "minutes")
    print(f"✓ Test 4 PASSED: CalculationUtils.extract_and_normalize_time('2 hours', 'minutes') = {result}")
except Exception as e:
    print(f"✗ Test 4 FAILED: {e}")
    sys.exit(1)

# Test 5: Metrics calculation
try:
    project_data = {
        'scale': '3500+ VMs, 存储约 1.5 TB',
        'customer': 'Test Customer'
    }
    metrics = utils.calculate_metrics(project_data)
    print(f"✓ Test 5 PASSED: CalculationUtils.calculate_metrics() returned:")
    for key, value in metrics.items():
        print(f"    {key}: {value}")
except Exception as e:
    print(f"✗ Test 5 FAILED: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("ALL TESTS PASSED!")
print("=" * 60)