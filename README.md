📌 Python Data Processing Macro Tool
📖 프로젝트 소개

본 프로젝트는 반복적인 데이터 가공 작업을 자동화하기 위한 Python 기반 매크로 툴입니다.
주로 PCB 설계, CAM 데이터, Netlist, Excel 데이터 등 다양한 텍스트 데이터를 빠르게 변환하기 위해 제작되었습니다.

GUI 기반으로 구성되어 있어 복잡한 코딩 없이도 다양한 데이터 처리를 수행할 수 있습니다.

🧩 주요 기능
1. 문자열 및 데이터 가공
숫자/문자 분리 및 재조합
숫자 자리수 자동 보정 (Zero Fill)
특정 문자열 포함 데이터만 변환
데이터 병합 및 분리
행/열 재정렬
2. 데이터 구조 변환
Tab 기반 데이터 재배열
일정 간격으로 라인 삽입
데이터 로테이션 (Row ↔ Column)
중복 데이터 정리 및 필터링
3. PCB / CAM / NET 데이터 처리
ORCAD Netlist 분석 및 변환
CAM DATA LIST 추출
Net 데이터 매칭 및 비교
채널 데이터 정리 및 병합
4. AutoCAD 자동화
좌표 데이터를 기반으로 .scr 파일 생성
Circle / Text 자동 생성 스크립트 출력
5. DXF → PCAD 데이터 변환
DXF 파일 내 CIRCLE 객체 추출
PCAD PAD 데이터 자동 생성

🛠 사용 기술
Python 3.x
Tkinter (GUI)
Clipboard 기반 데이터 처리
정규표현식 (re)
DXF 처리 (ezdxf)

📦 필요 라이브러리
pip install xlrd pywin32 pygetwindow clipboard getmac ezdxf setuptools
📁 프로젝트 구조
project/
│
├── main.py (메인 실행 파일)
└── DXFTOPCADPAD.py        ← 수정 금지 (외부 연동)

⚠️ 주의사항

아래 파일은 수정 금지
DXFTOPCADPAD.py

대부분 기능은 클립보드 기반으로 동작
→ 복사 → 실행 → 붙여넣기 구조
