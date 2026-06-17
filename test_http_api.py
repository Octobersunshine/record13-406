import urllib.request
import urllib.error
import time
import subprocess
import sys


def main():
    proc = subprocess.Popen(
        [sys.executable, 'trig_service.py', 'http', '8082'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(1.5)

    test_cases = [
        ('/sin?value=inf', 400, 'infinity'),
        ('/sin?value=nan', 400, 'NaN'),
        ('/asin?value=2', 400, 'range'),
        ('/cos?value=hello', 400, 'number'),
        ('/sin?value=90&unit=degree', 200, None),
        ('/invalid_func?value=1', 400, 'Unsupported'),
        ('/tan?value=inf&unit=degree', 400, 'infinity'),
        ('/acos?value=nan', 400, 'NaN'),
        # Hyperbolic function tests
        ('/sinh?value=0', 200, None),
        ('/cosh?value=0', 200, None),
        ('/tanh?value=0', 200, None),
        ('/sinh?value=1', 200, None),
        ('/cosh?value=1', 200, None),
        ('/tanh?value=1', 200, None),
        ('/sinh?value=180&unit=degree', 200, None),
        ('/cosh?value=inf', 400, 'infinity'),
        ('/tanh?value=nan', 400, 'NaN'),
    ]

    print('=== HTTP API Error Handling Tests ===')
    print()
    all_passed = True

    for path, expected_status, expected_substr in test_cases:
        url = f'http://localhost:8082{path}'
        try:
            with urllib.request.urlopen(url) as resp:
                status = resp.status
                body = resp.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            status = e.code
            body = e.read().decode('utf-8')
        except Exception as e:
            status = 'ERROR'
            body = str(e)

        status_ok = status == expected_status
        substr_ok = True
        if expected_substr:
            substr_ok = expected_substr.lower() in body.lower()

        passed = status_ok and substr_ok
        if not passed:
            all_passed = False

        status_mark = '✓' if status_ok else '✗'
        substr_mark = '✓' if substr_ok else '✗'

        print(f'GET {path}')
        print(f'  Status: {status} (expected {expected_status}) {status_mark}')
        if expected_substr:
            print(f'  Contains "{expected_substr}": {substr_mark}')
        print(f'  Body: {body[:150]}')
        print()

    proc.terminate()
    try:
        proc.wait(timeout=3)
    except Exception:
        proc.kill()

    if all_passed:
        print('✅ All HTTP tests passed!')
    else:
        print('❌ Some tests failed!')
        sys.exit(1)


if __name__ == '__main__':
    main()
