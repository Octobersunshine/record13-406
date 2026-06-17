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


def test_invalid_inputs():
    print("=== Testing Invalid Inputs ===")
    
    # Test inf
    try:
        TrigCalculator.sin(float('inf'))
        assert False, "sin(inf) should raise ValueError"
    except ValueError as e:
        print(f"sin(inf) raises ValueError: {e}")
    
    try:
        TrigCalculator.cos(float('-inf'))
        assert False, "cos(-inf) should raise ValueError"
    except ValueError as e:
        print(f"cos(-inf) raises ValueError: {e}")
    
    # Test nan
    try:
        TrigCalculator.sin(float('nan'))
        assert False, "sin(nan) should raise ValueError"
    except ValueError as e:
        print(f"sin(nan) raises ValueError: {e}")
    
    try:
        TrigCalculator.tan(float('nan'), 'degree')
        assert False, "tan(nan) should raise ValueError"
    except ValueError as e:
        print(f"tan(nan) raises ValueError: {e}")
    
    # Test inverse function domain violation
    try:
        TrigCalculator.asin(2.0)
        assert False, "asin(2) should raise ValueError"
    except ValueError as e:
        print(f"asin(2) raises ValueError: {e}")
    
    try:
        TrigCalculator.asin(-2.0, 'degree')
        assert False, "asin(-2) should raise ValueError"
    except ValueError as e:
        print(f"asin(-2) raises ValueError: {e}")
    
    try:
        TrigCalculator.acos(1.5)
        assert False, "acos(1.5) should raise ValueError"
    except ValueError as e:
        print(f"acos(1.5) raises ValueError: {e}")
    
    # Test invalid input type
    try:
        TrigCalculator.sin("hello")
        assert False, "sin('hello') should raise ValueError"
    except ValueError as e:
        print(f"sin('hello') raises ValueError: {e}")
    
    # Test hyperbolic inf/nan
    try:
        TrigCalculator.sinh(float('inf'))
        assert False, "sinh(inf) should raise ValueError"
    except ValueError as e:
        print(f"sinh(inf) raises ValueError: {e}")
    
    try:
        TrigCalculator.cosh(float('nan'))
        assert False, "cosh(nan) should raise ValueError"
    except ValueError as e:
        print(f"cosh(nan) raises ValueError: {e}")
    
    print()


def test_hyperbolic():
    print("=== Testing Hyperbolic Functions ===")
    
    pi = math.pi
    
    # sinh(0) = 0
    sinh_0 = TrigCalculator.sinh(0, 'radian')
    print(f"sinh(0) = {sinh_0} (expected ~0.0)")
    assert abs(sinh_0 - 0.0) < 1e-10, "sinh(0) test failed"
    
    # sinh(1) using math.sinh directly for comparison
    sinh_1 = TrigCalculator.sinh(1.0, 'radian')
    expected_sinh_1 = math.sinh(1.0)
    print(f"sinh(1) = {sinh_1} (expected ~{expected_sinh_1})")
    assert abs(sinh_1 - expected_sinh_1) < 1e-10, "sinh(1) test failed"
    
    # cosh(0) = 1
    cosh_0 = TrigCalculator.cosh(0, 'radian')
    print(f"cosh(0) = {cosh_0} (expected ~1.0)")
    assert abs(cosh_0 - 1.0) < 1e-10, "cosh(0) test failed"
    
    # cosh(1)
    cosh_1 = TrigCalculator.cosh(1.0, 'radian')
    expected_cosh_1 = math.cosh(1.0)
    print(f"cosh(1) = {cosh_1} (expected ~{expected_cosh_1})")
    assert abs(cosh_1 - expected_cosh_1) < 1e-10, "cosh(1) test failed"
    
    # tanh(0) = 0
    tanh_0 = TrigCalculator.tanh(0, 'radian')
    print(f"tanh(0) = {tanh_0} (expected ~0.0)")
    assert abs(tanh_0 - 0.0) < 1e-10, "tanh(0) test failed"
    
    # tanh(1)
    tanh_1 = TrigCalculator.tanh(1.0, 'radian')
    expected_tanh_1 = math.tanh(1.0)
    print(f"tanh(1) = {tanh_1} (expected ~{expected_tanh_1})")
    assert abs(tanh_1 - expected_tanh_1) < 1e-10, "tanh(1) test failed"
    
    # Test with degree unit: sinh(π radians) = sinh(180 degrees)
    sinh_pi = TrigCalculator.sinh(pi, 'radian')
    sinh_180 = TrigCalculator.sinh(180, 'degree')
    print(f"sinh(π rad) = {sinh_pi}, sinh(180°) = {sinh_180} (should be equal)")
    assert abs(sinh_pi - sinh_180) < 1e-10, "sinh degree/radian equivalence test failed"
    
    # cosh²(x) - sinh²(x) = 1 identity
    x = 2.5
    sinh_x = TrigCalculator.sinh(x)
    cosh_x = TrigCalculator.cosh(x)
    identity = cosh_x ** 2 - sinh_x ** 2
    print(f"cosh²({x}) - sinh²({x}) = {identity} (expected ~1.0)")
    assert abs(identity - 1.0) < 1e-10, "Hyperbolic identity test failed"
    
    print()


if __name__ == '__main__':
    test_basic_trig()
    test_inverse_trig()
    test_roundtrip()
    test_invalid_inputs()
    test_hyperbolic()
    print("✅ All tests passed!")
