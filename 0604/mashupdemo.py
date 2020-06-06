#Mash-up
import tkinter
import tkinter.ttk
import json
import urllib.request
import urllib.parse

filename = 'subwayinfo.json'
seoul_id = '4a4755416c64657637315a71736363' #서울데이터광장의 Open API를 사용하기 위한 인증키
Seoul_URL = 'http://openapi.seoul.go.kr:8088/'    #서울데이터광장의 [서울특별시 노선별 지하철역 정보]를 위한 URL

naver_url = 'file://localhost/json'   #비로그인 오픈 API를 사용하기 위한 웹 서비스 URL
naver_id = 'U7rIakMlAOCbBnyhKziB'  #Naver client_id
naver_secret_ = '2j4tzGC_nQ'   #Naver Client_Secret
naver_local_search_url = 'https://openapi.naver.com/v1/search/local.json?query='

def change_line(*args):
    line = comboLine.get()   #1호선
    set_stations(line)

def set_stations(line):
    line = urllib.parse.quote(line)
    url = Seoul_URL
    url += seoul_id + '/json/SearchSTNBySubwayLineInfo/0/100/%20/%20/' + line
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            result = response_body.decode('utf-8')
            result = json.loads(result)
            point = result['SearchSTNBySubwayLineInfo']
            station = []
            for i in point['row']:   #list
                station.append(i['STATION_NM'] + "역")
            comboStation['values'] = tuple(station)
            comboStation.current(0)

        else : 
            print('Error Code : ' + rescode)
    except:
        print('Seoul Exception')


def getLineInfo():   # 수도권 전철 노선명을 Tuple로 return 해야 함.   
    try:
        with open(filename, 'rt', encoding='utf-8') as ptr:
            json_data = json.load(ptr)
            list_ = json_data['DATA']
            station = []
            for row in list_ :    #row는 dict다.
                line = row['line_num']  #2호선
                if not (line in station):  #없으면
                    station.append(line)
            for (idx, data) in enumerate(station):
                if data.startswith('0') : 
                    data = data.lstrip('0')
                    station[idx] = data
            station.sort()
    except:
        print('File Exception')
    else:
        return tuple(station)

def search_place():
    #선택한 역과 검색어
    keyword = comboStation.get().strip() + entry.get().strip()
    url = naver_local_search_url + urllib.parse.quote(keyword)  #선택한 역과 검색어를 utf-8로 encoding
    request = urllib.request.Request(url)
    request.add_header('Content-Type', 'application/json')
    request.add_header('X-Naver-Client-Id', naver_id)
    request.add_header('X-Naver-Client-Secret', naver_secret_) 
    
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            result = response_body.decode('utf-8')
            json_data = json.loads(result)
            # #먼저 treeview를 clear한다.
            treeview.delete(*treeview.get_children())
            for row in json_data['items']:
                treeview.insert('', 'end', iid=None, text=row['title'],
                values=[row['category'], row['telephone'], row['roadAddress'], 
                row['description'], row['mapx'], row['mapy']])
        else :
            print('Error code : ' + rescode)
    except:
        print('Naver Search Exception')
        
app = tkinter.Tk()
app.title('지하철 역주변 편의시설 검색 서비스')
app.geometry('800x800')
app.resizable(0,0)

labelTitle = tkinter.Label(app, text='편의 시설 알리미', font=('맑은 고딕', 15))
labelTitle.pack(side=tkinter.TOP, pady=5)
labelLine = tkinter.Label(app, text='노선번호', font=('맑은 고딕', 10))
labelLine.place(x=50, y=60, width=120, height=25)
labelStation = tkinter.Label(app, text='역이름', font=('맑은 고딕', 10))
labelStation.place(x=250, y=60, width=120, height=25)
labelPlace = tkinter.Label(app, text='편의시설', font=('맑은 고딕', 10))
labelPlace.place(x=500, y=60, width=120, height=25)

strLine = tkinter.StringVar()

comboLine = tkinter.ttk.Combobox(app, textvariable=strLine, values=getLineInfo())
comboLine.place(x=50, y=90, width=120, height=25)
comboLine.current(0)

#comboLine의 특정 지하철 노선을 선택하면 발생하는 이벤트 처리
comboLine.bind('<<ComboboxSelected>>', change_line)

strStation = tkinter.StringVar()
comboStation = tkinter.ttk.Combobox(app, textvariable=strStation)
comboStation.place(x=220, y=90, width=200, height=25)

strEntry = tkinter.StringVar()
entry = tkinter.Entry(app, textvariable=strEntry, width=20, font=('맑은 고딕', 15))
entry.place(x=470, y=90, width=200, height=25)

btnSearch = tkinter.Button(app, text='검색', command=search_place, font=('맑은 고딕', 15))
btnSearch.place(x=700, y=90, width=80, height=25)

treeview = tkinter.ttk.Treeview(app)
treeview['columns'] = ('category', 'telephone')
treeview.column('category', width=100)
treeview.column('telephone', width=100)

treeview.heading('#0', text='상호명')
treeview.heading('category', text='분류')
treeview.heading('telephone', text = '전화번호')
treeview.place(x=50, y=140, width=700, height=300)



app.mainloop()