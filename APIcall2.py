import requests, sys, json, re

URL = "https://re.jrc.ec.europa.eu/api/"
VALID_ARGUMENTS = ["batterysize","month", "cutoff","consumptionday", "lat", "usehorizon", "lon", "userhorizon", "raddatabase", "peakpower", "pvtechchoice", "mountingplace", "loss", "fixed", "angle", "aspect", "optimalinclination", "optimalangles", "inclined_axis", "inclined_optimum", "inclinedaxisangle", "vertical_axis", "vertical_optimum", "verticalaxisangle", "twoaxis", "pvprice", "systemcost", "interest", "lifetime", "outputformat", "browser"]



def get_url():
    if "--tool_name" not in sys.argv:
        print("Please provide the --tool_name argument: 'PVcalc, SHScalc, MRcalc, DRcalc, seriescalc, tmy, printhorizon'")
        sys.exit(1)

    tool_name_index = sys.argv.index("--tool_name")

    tool_name = sys.argv[tool_name_index + 1]

    base_url = f"{URL + tool_name}?"

    url = base_url
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        value = sys.argv[i + 1] if i + 1 < len(sys.argv) else ""

        if arg.startswith("--") and arg[2:] in VALID_ARGUMENTS:
            url += f"{arg[2:]}={value}&"

        i += 2

    url = url.rstrip("&")

    print("API URL:", url)
    return url

def API_request(url):
    res = requests.get(url)
    if "json" in sys.argv:
        print(res.json())
        return res.json()
    
    print(res.text)
    return res.text

def main():
    if len(sys.argv) == 1:
        print('----------***********----------')
        print("\nUsage: python script.py --tool_name <value> --arg1 <value> --arg2 <value> ...\n")
        print('----------***********----------')
        print("Options:\n")
        print("--tool_name\t\tSpecify the tool name (required): PVcalc, SHScalc, MRcalc, DRcalc, seriescalc, tmy, printhorizon\n")
        print("--arg1\t\tSpecify argument 1\n")
        print("You can specify the outpy format using --outputformat <your format>\nThe format supported: csv - basic - json")
        print('\n----------***********----------')
        print("Exemple: \npython3 APIcall.py --tool_name PVcalc --lat 45 --lon 8 --peakpower 1 --loss 14\n")
        print("python3 APIcall.py --tool_name SHScalc --lat 45 --lon 8 --peakpower 10 --batterysize 50 --consumptionday 200 --cutoff 40")
        print("python3 APIcall.py --tool_name DRcalc --lat 45 --lon 8 --month 3 --global 1")
        print("python3 APIcall.py --tool_name MRcalc --lat 45 --lon 8 --horirrad 1")
        print('----------***********----------')
        print('')
        print(f'Valid arguments: {(VALID_ARGUMENTS)}')
        sys.exit(0)
    url = get_url()
    body = API_request(url)

main()