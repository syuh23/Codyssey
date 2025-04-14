# 전역변수
material = ""
diameter = 0
thickness = 0
area = 0
weight = 0

# 재질 - 무게 저장
material_density = {
    "유리" : 2.4,
    "알루미늄" : 2.7,
    "탄소강" : 7.85
}

# sphere_area 함수 구현
def sphere_area(diameter, material, thickness):
    
    global area, weight
    
    if diameter <= 0:
        print("지름은 0보다 커야 합니다 !")
        return
    
    radius = diameter / 2
    area_m = 2 * 3.1415926535 * (radius ** 2)
    area_cm = (area_m) * 10000
    
    density = material_density.get(material, 2.4)
    volume_cm3 = area_cm * thickness
    weight_g = volume_cm3 * density
    weight_kg = (weight_g / 1000) * 0.38
    
    globals()["material"] = material
    globals()["diameter"] = diameter
    globals()["thickness"] = thickness
    area = round(area_m, 3)
    weight = round(weight_kg, 3)
    
    print(f"재질 => {material}, 지름 => {diameter}, 두께 => {thickness}, 면적 => {area}, 무게 => {weight} kg")

# main 로직
while True:
    try:
        input_diameter = input("지름을 입력하세요 (종료하려면 'exit'): ")
        if input_diameter.lower() == 'exit':
            print("프로그램을 종료합니다.")
            break

        diameter = float(input_diameter)

        material_input = input("재질을 입력하세요 (유리/알루미늄/탄소강, 기본=유리): ")
        if material_input == "":
            material_input = "유리"

        thickness_input = input("두께를 입력하세요 (cm, 기본=1): ")
        if thickness_input == "":
            thickness = 1
        else:
            thickness = float(thickness_input)

        sphere_area(diameter, material_input, thickness)

    except ValueError:
        print("올바른 값을 입력해주세요.")