import matplotlib.pyplot as plt
import csv

# CSV 파일에서 데이터 읽기
data_file = "C:\\Users\\user\\Desktop\\2023-School-Projects\\H-R Diagram\\StarData.csv"  # 파일 경로를 적절히 변경하세요.
tems = []
lums = []

with open(data_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # 헤더 건너뛰기

    for row in csv_reader:
        temperature = float(row[0])
        luminosity = float(row[1])
        tems.append(temperature)
        lums.append(luminosity)

# 그래프 그리기
plt.figure(figsize=(10, 10))
plt.scatter(tems, lums, color='blue', marker='o')

# 축 범위 설정
plt.yscale('log')  # Y축에 로그 스케일 적용
plt.xlim(30000, 300)  # X축 범위 설정
plt.ylim(1e-6, 1e6)  # Y축 범위 설정

# 축 이름 추가
plt.xlabel('Temperature (K)')
plt.ylabel('Luminosity (compared to Sun)')

# 그래프 표시
plt.title('H-R')
plt.grid(True)
plt.show()
