import tkinter as tk
from tkinter import filedialog
import ezdxf
import os


if __name__ == "__main__":
    def select_file():
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("DXF files", "*.dxf")])
        return file_path

    file_path = select_file()

    if file_path:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()
        circles = msp.query('CIRCLE')
        cdata = []
        for circle in circles:
            center = circle.dxf.center
            diameter = round(circle.dxf.radius * 2,4)
            cdata.append([center[0], center[1], diameter])
    else:
        print("No file selected.")


    with open('PCADPAD기본데이터.TXT', 'r', encoding='utf-8') as f:
        data = f.read().splitlines()

    # clipboard_data = pyperclip.paste()
    # clip_data = [line.split('\t') for line in clipboard_data.split('\n') if line.strip()]
    # result = [[float(x), float(y), float(diameter)] for x, y, diameter in clip_data]
    result = cdata

    # '(PADDATA)' 항목의 인덱스 찾기
    index = data.index('    (PADDATA)')
    for x, y, diameter in result:
        pad_data = (f'    (pad (padNum 0) (padStyleRef "{diameter}") (pt {x} {y}) )')
        data[index+1:index+1] = [pad_data]

    data.remove('    (PADDATA)')

    # '(PADLIST DATA)' 항목의 인덱스 찾기
    index = data.index('  (PADLIST DATA)')

    # '(PADLIST DATA)' 항목 이후에 내가 추가하고자 하는 텍스트 삽입
    diameter_list = list(set([d for _, _, d in result]))
    for diameter in diameter_list:
        pad_list = (f'  (padStyleDef "{diameter}"\n    (holeDiam 0.1)\n    (StartRange 1)\n    (EndRange 2)\n    (padShape (layerNumRef 1) (padShapeType Ellipse) (shapeWidth {diameter}) (shapeHeight {diameter}) )\n    (padShape (layerNumRef 2) (padShapeType Ellipse) (shapeWidth 1.524) (shapeHeight 1.524) )\n    (padShape (layerType Signal) (padShapeType Ellipse) (shapeWidth 1.524) (shapeHeight 1.524) )\n    (padShape (layerType Plane) (padShapeType Thrm4_45) (outsideDiam 2.1336) (insideDiam 1.524) (spokeWidth 0.381) )\n    (padShape (layerType NonSignal) (padShapeType Ellipse) (shapeWidth 0.0) (shapeHeight 0.0) )\n  )')
        data[index+1:index+1] = [pad_list]
    data.remove('  (PADLIST DATA)')

    # 사용자 바탕화면 경로 가져오기
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # PCBDXF 폴더 생성
    folder_path = os.path.join(desktop_path, "PCBDXF")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # 파일 경로 생성
    file_path = os.path.join(folder_path, "output.pcb")

    # 폴더 열기
    os.startfile(os.path.dirname(file_path))

    # 파일 저장
    with open(file_path, 'w') as f:
        for item in data:
            f.write("%s\n" % item)