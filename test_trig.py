import math
from trig_service import TrigCalculator


def test_basic_trig():
    print("=== Testing Basic Trigonometric Functions ===")
    
    pi = math.pi
    
    sin_90 = TrigCalculator.sin(90, 'degree')
    print(f"sin(90°) = {sin_90} (expected ~1.0)")
    assert abs(sin_90 - 1.0) < 1e-10, "sin(90°) test failed"
    
    sin_pi_2 = TrigCalculator.sin(pi / 2, 'radian')
    print(f"sin(π/2) = {sin_pi_2} (expected ~1.0)")
    assert abs(sin_pi_2 - 1.0) < 1e-10, "sin(π/2) test failed"
    
    cos_0 = TrigCalculator.cos(0, 'degree')
    print(f"cos(0°) = {cos_0} (expected ~1.0)")
    assert abs(cos_0 - 1.0) < 1e-10, "cos(0°) test failed"
    
    cos_180 = TrigCalculator.cos(180, 'degree')
    print(f"cos(180°) = {cos_180} (expected ~-1.0)")
    assert abs(cos_180 - (-1.0)) < 1e-10, "cos(180°) test failed"
    
    tan_45 = TrigCalculator.tan(45, 'degree')
    print(f"tan(45°) = {tan_45} (expected ~1.0)")
    assert abs(tan_45 - 1.0) < 1e-10, "tan(45°) test failed"
    
    print()


def test_inverse_trig():
    print("=== Testing Inverse Trigonometric Functions ===")
    
    asin_result = TrigCalculator.asin(1.0, 'degree')
    print(f"asin(1.0) = {asin_result}° (expected ~90°)")
    assert abs(asin_result - 90.0) < 1e-10, "asin(1.0) test failed"
    
    asin_rad = TrigCalculator.asin(1.0, 'radian')
    print(f"asin(1.0) = {asin_rad} rad (expected ~π/2)")
    assert abs(asin_rad - math.pi / 2) < 1e-10, "asin(1.0) rad test failed"
    
    acos_result = TrigCalculator.acos(1.0, 'degree')
    print(f"acos(1.0) = {acos_result}° (expected ~0°)")
    assert abs(acos_result - 0.0) < 1e-10, "acos(1.0) test failed"
    
    acos_0 = TrigCalculator.acos(0.0, 'degree')
    print(f"acos(0.0) = {acos_0}° (expected ~90°)")
    assert abs(acos_0 - 90.0) < 1e-10, "acos(0.0) test failed"
    
    atan_result = TrigCalculator.atan(1.0, 'degree')
    print(f"atan(1.0) = {atan_result}° (expected ~45°)")
    assert abs(atan_result - 45.0) < 1e-10, "atan(1.0) test failed"
    
    print()


def test_roundtrip():
    print("=== Testing Roundtrip (sin -> asin) ===")
    
    angle_deg = 30.0
    sin_val = TrigCalculator.sin(angle_deg, 'degree')
    recovered = TrigCalculator.asin(sin_val, 'degree')
    print(f"sin({angle_deg}°) = {sin_val}, asin({sin_val}) = {recovered}°")
    assert abs(recovered - angle_deg) < 1e-10, "Roundtrip test failed"
    
    angle_rad = math.pi / 4
    sin_val_rad = TrigCalculator.sin(angle_rad, 'radian')
    recovered_rad = TrigCalculator.asin(sin_val_rad, 'radian')
    print(f"sin(π/4) = {sin_val_rad}, asin({sin_val_rad}) = {recovered_rad} rad")
    assert abs(recovered_rad - angle_rad) < 1e-10, "Roundtrip rad test failed"
    
    print()


if __name__ == '__main__':
    test_basic_trig()
    test_inverse_trig()
    test_roundtrip()
    print("✅ All tests passed!")
