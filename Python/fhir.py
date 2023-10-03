import iris
import argparse

def GETTest(id):
    iris.cls('developer.Test').GETTest(id)

def SearchTest(patientId):
    iris.cls('developer.Test').SearchTest(patientId)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('function_name', type=str, help='set fuction name in this file')
    parser.add_argument('-i', '--func_args', nargs='*', help='args in function', default=[])
    args = parser.parse_args()

    func_dict = {k: v for k, v in locals().items() if callable(v)}
    func_args = [float(x) if x.isnumeric() else x for x in args.func_args]

    ret = func_dict[args.function_name](*func_args)
