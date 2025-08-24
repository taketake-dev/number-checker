# main.py

# ユーザーに入力を促す
user_input = input("数字を入力してください: ")

try:
    # 入力された文字列を整数に変換
    number = int(user_input)

    # 2で割った余りが0かどうかで偶数・奇数を判断
    if number % 2 == 0:
        print(f"{number} は偶数です。")
    else:
        print(f"{number} は奇数です。")

except ValueError:
    # 整数に変換できなかった場合のエラー処理
    print("エラー: 数字以外が入力されました。")
    