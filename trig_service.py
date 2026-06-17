import math
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import sys


class TrigCalculator:
    @staticmethod
    def _to_radians(value, unit):
        if unit == 'degree':
            return math.radians(value)
        return value

    @staticmethod
    def _from_radians(value, unit):
        if unit == 'degree':
            return math.degrees(value)
        return value

    @staticmethod
    def sin(value, unit='radian'):
        rad = TrigCalculator._to_radians(value, unit)
        return math.sin(rad)

    @staticmethod
    def cos(value, unit='radian'):
        rad = TrigCalculator._to_radians(value, unit)
        return math.cos(rad)

    @staticmethod
    def tan(value, unit='radian'):
        rad = TrigCalculator._to_radians(value, unit)
        return math.tan(rad)

    @staticmethod
    def asin(value, unit='radian'):
        result = math.asin(value)
        return TrigCalculator._from_radians(result, unit)

    @staticmethod
    def acos(value, unit='radian'):
        result = math.acos(value)
        return TrigCalculator._from_radians(result, unit)

    @staticmethod
    def atan(value, unit='radian'):
        result = math.atan(value)
        return TrigCalculator._from_radians(result, unit)


class TrigHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        func = parsed.path.lstrip('/').lower()
        supported_funcs = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']

        if func not in supported_funcs:
            self._send_error(400, f'Unsupported function: {func}. Supported: {supported_funcs}')
            return

        if 'value' not in params:
            self._send_error(400, 'Missing required parameter: value')
            return

        try:
            value = float(params['value'][0])
        except (ValueError, IndexError):
            self._send_error(400, 'Invalid parameter: value must be a number')
            return

        unit = params.get('unit', ['radian'])[0].lower()
        if unit not in ['radian', 'degree']:
            self._send_error(400, 'Invalid unit: must be "radian" or "degree"')
            return

        try:
            calc_method = getattr(TrigCalculator, func)
            result = calc_method(value, unit)
        except ValueError as e:
            self._send_error(400, f'Calculation error: {str(e)}')
            return

        response = {
            'function': func,
            'input': value,
            'unit': unit,
            'result': result
        }
        self._send_json(response)

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def _send_error(self, status, message):
        self._send_json({'error': message}, status)

    def log_message(self, format, *args):
        pass


def run_http_server(host='0.0.0.0', port=8080):
    server = HTTPServer((host, port), TrigHTTPRequestHandler)
    print(f'Trigonometry HTTP Service running at http://{host}:{port}')
    print('Supported endpoints: /sin, /cos, /tan, /asin, /acos, /atan')
    print('Query params: value (number), unit (radian|degree, default: radian)')
    print('Example: http://localhost:8080/sin?value=90&unit=degree')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')


def run_cli():
    print('Trigonometry Calculator (CLI Mode)')
    print('Supported functions: sin, cos, tan, asin, acos, atan')
    print('Type "quit" or "exit" to stop\n')

    while True:
        try:
            func = input('Enter function (sin/cos/tan/asin/acos/atan): ').strip().lower()
            if func in ('quit', 'exit'):
                print('Goodbye!')
                break
            if func not in ('sin', 'cos', 'tan', 'asin', 'acos', 'atan'):
                print('Invalid function. Try again.\n')
                continue

            value_str = input('Enter value: ').strip()
            try:
                value = float(value_str)
            except ValueError:
                print('Invalid number. Try again.\n')
                continue

            unit = input('Enter unit (radian/degree, default radian): ').strip().lower()
            if unit not in ('radian', 'degree'):
                unit = 'radian'

            calc_method = getattr(TrigCalculator, func)
            result = calc_method(value, unit)
            print(f'\nResult: {func}({value} {unit}) = {result}\n')

        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            break
        except ValueError as e:
            print(f'Calculation error: {e}\n')


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'http':
        port = 8080
        if len(sys.argv) > 2:
            try:
                port = int(sys.argv[2])
            except ValueError:
                pass
        run_http_server(port=port)
    else:
        run_cli()


if __name__ == '__main__':
    main()
