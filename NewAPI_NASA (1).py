import os, json, requests,pandas as pd

locations = [(5, 10)]

output = r"D:\Temp"
base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2MDEW,T2MWET,TS,T2M_RANGE,T2M_MAX,T2M_MIN&community=RE&longitude={longitude}&latitude={latitude}&start=20150101&end=20150305&format=JSON"


def NewAPI2_ReadSolarNasa(pk_id,output,_start_date,_end_date,longitude,latitude):

    base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?"
    url_line1 = "parameters=T2M_MAX,T2M_MIN,T2M,PRECTOTCORR,TS_MAX,TS_MIN,TS,RH2M,T2MDEW,WS2M,ALLSKY_SFC_SW_DWN,GWETPROF"
    url_line2 = "&community=RE&longitude={longitude}&latitude={latitude}&start={start_date}&end={end_date}&format={output}"
    load_url = base_url+url_line1+url_line2
    
    api_request_url = load_url.format(start_date = _start_date,end_date = _end_date,longitude=longitude, latitude=latitude, output=output.upper())
    print(api_request_url)
    response = requests.get(url=api_request_url, verify=True, timeout=30.00)
    content = json.loads(response.content.decode('utf-8'))
    nasa_df = pd.DataFrame.from_dict(content['properties']['parameter'])
    nasa_df.index = pd.to_datetime(nasa_df.index)
    nasa_df.index.name = 'DATE'
    print(nasa_df)
    filename = response.headers['content-disposition'].split('filename=')[1]
    filename = filename.replace('json','csv')
    fcsv = os.path.join(r"D:\Temp", filename)
    print(filename,fcsv)
    nasa_df.to_csv(fcsv)

NewAPI2_ReadSolarNasa(1,"json","20200101","20201201",100.34343,16.00000)
