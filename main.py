import random

def display_instructions():
    print("歡迎來到簡易高爾夫遊戲!")
    print("你需要將球擊入洞中。")
    print("每次你可以選擇擊球的力度 (1-10)。")
    print("祝你好運!\n")

def take_shot():
    while True:
        try:
            shot = int(input("請選擇你的擊球力度 (1-10): "))
            if 1 <= shot <= 10:
                break
            else:
                print("請輸入 1 到 10 之間的數字。")
        except ValueError:
            print("請輸入一個有效的數字。")
    return shot

def play_golf_game():
    hole_distance = random.randint(50, 150)  # 隨機生成洞的距離
    current_distance = 0  # 球的初始位置
    total_shots = 0  # 記錄總擊球次數

    display_instructions()

    print(f"洞的距離是 {hole_distance} 碼。\n")

    while current_distance < hole_distance:
        shot_power = take_shot()
        shot_distance = shot_power * random.randint(8, 12)  # 擊球距離隨機波動
        current_distance += shot_distance
        total_shots += 1
        print(f"你擊球 {shot_distance} 碼。")
        print(f"球現在在 {current_distance} 碼處。")
        
        if current_distance >= hole_distance:
            break
        else:
            print("你還沒有進洞，請繼續擊球。\n")

    print(f"恭喜你! 你用了 {total_shots} 杆將球送入洞中。")

if __name__ == "__main__":
    play_golf_game()
