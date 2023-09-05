from flaskr import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # 食材のデータ
    ingredients = {
        'ふといながねぎ': 0,
        'あじわいキノコ': 0,
        'とくせんエッグ': 0,
        'ほっこりポテト': 0,
        'とくせんリンゴ': 0,
        'げきからハーブ': 0,
        'マメミート': 0,
        'モーモーミルク': 0,
        'あまいミツ': 0,
        'ピュアなオイル': 0,
        'あったかジンジャー': 0,
        'あんみんトマト': 0,
        'リラックスカカオ': 0,
        'おいしいシッポ': 0,
        'ワカクサ大豆': 0,
    }
    
    # カレー・シチューのレシピ
    curry_recipes = [
        {'ingredients': {'とくせんリンゴ': 7}, 'num': 7, 'dish': 'とくせんリンゴカレー', 'energy': 668},
        {'ingredients': {'モーモーミルク': 7}, 'num': 7, 'dish': 'たんじゅんホワイトシチュー', 'energy': 727},
        {'ingredients': {'あまいミツ': 7}, 'num': 7, 'dish': 'ベイビィハニーカレー', 'energy': 749},
        {'ingredients': {'マメミート': 7}, 'num': 7, 'dish': 'マメバーグカレー', 'energy': 764},
        {'ingredients': {'モーモーミルク': 8, 'マメミート': 8}, 'num': 16, 'dish': '満腹チーズバーグカレー', 'energy': 1785},
        {'ingredients': {'マメミート': 10, 'ピュアなオイル': 5}, 'num': 15, 'dish': 'ひでりカツカレー', 'energy': 1815},
        {'ingredients': {'あんみんトマト': 10, 'げきからハーブ': 5}, 'num': 15, 'dish': 'サンパワートマトカレー', 'energy': 1943},
        {'ingredients': {'とくせんエッグ': 10, 'あんみんトマト': 6}, 'num': 16, 'dish': 'とけるオムカレー', 'energy': 2009},
        {'ingredients': {'モーモーミルク': 10, 'ほっこりポテト': 8, 'あじわいキノコ': 4}, 'num': 22, 'dish': 'ほっこりポテトシチュー', 'energy': 3089},
        {'ingredients': {'ワカクサ大豆': 12, 'マメミート': 6, 'とくせんエッグ': 4, 'げきからハーブ': 4}, 'num': 26, 'dish': 'ビルドアップマメカレー', 'energy': 3274},
        {'ingredients': {'あじわいキノコ': 14, 'ほっこりポテト': 9}, 'num': 23, 'dish': 'キノコのほうしカレー', 'energy': 4041},
        {'ingredients': {'あまいミツ': 12, 'とくせんリンゴ': 11, 'とくせんエッグ': 8, 'ほっこりポテト': 4}, 'num': 35, 'dish': 'おやこあいカレー', 'energy': 4523},
        {'ingredients': {'ふといながねぎ': 14, 'あったかジンジャー': 10, 'げきからハーブ': 8}, 'num': 32, 'dish': 'げきからネギカレー', 'energy': 5900},
        {'ingredients': {'ワカクサ大豆': 15, 'ふといながねぎ': 9, 'マメミート': 9, 'あじわいキノコ': 5}, 'num': 38, 'dish': 'にんじゃカレー', 'energy': 6159},
        {'ingredients': {'げきからハーブ': 25, 'おいしいシッポ': 8}, 'num': 33, 'dish': 'ヤドンのシッポカレー', 'energy': 7483},
        {'ingredients': {'リラックスカカオ': 12, 'モーモーミルク': 10, 'ほっこりポテト': 18, 'あんみんトマト': 15}, 'num': 55, 'dish': 'ぜったいねむりバターカレー', 'energy': 9010},
    ]

    # サラダのレシピ
    salad_recipes = [
        {'ingredients': {'とくせんリンゴ': 8}, 'num': 8, 'dish': 'とくせんリンゴサラダ', 'energy': 763},
        {'ingredients': {'マメミート': 8}, 'num': 8, 'dish': 'マメハムサラダ', 'energy': 873},
        {'ingredients': {'あんみんトマト': 8}, 'num': 8, 'dish': 'あんみんトマトサラダ', 'energy': 933},
        {'ingredients': {'モーモーミルク': 10, 'マメミート': 6}, 'num': 16, 'dish': 'ゆきかきシーザーサラダ', 'energy': 1774},
        {'ingredients': {'ワカクサ大豆': 10, 'あんみんトマト': 6}, 'num': 16, 'dish': 'うるおいとうふサラダ', 'energy': 1843},
        {'ingredients': {'ワカクサ大豆': 10, 'げきからハーブ': 6}, 'num': 16, 'dish': 'ねっぷうとうふサラダ', 'energy': 1976},
        {'ingredients': {'モーモーミルク': 5, 'ピュアなオイル': 3, 'とくせんリンゴ': 15}, 'num': 23, 'dish': 'メロメロりんごのチーズサラダ', 'energy': 2578},
        {'ingredients': {'ふといながねぎ': 12, 'あったかジンジャー': 5}, 'num': 15, 'dish': 'めんえきネギサラダ', 'energy': 2658},
        {'ingredients': {'モーモーミルク': 12, 'ピュアなオイル': 5, 'あんみんトマト': 6}, 'num': 23, 'dish': 'モーモーカプレーゼ', 'energy': 2856},
        {'ingredients': {'マメミート': 9, 'あったかジンジャー': 6, 'とくせんエッグ': 5, 'ほっこりポテト': 3}, 'num': 23, 'dish': 'からげんきサラダ', 'energy': 2958},
        {'ingredients': {'リラックスカカオ': 14, 'マメミート': 9}, 'num': 23, 'dish': 'ムラっけチョコレートサラダ', 'energy': 3558},
        {'ingredients': {'ほっこりポテト': 14, 'とくせんエッグ': 9, 'マメミート': 7, 'とくせんリンゴ': 6}, 'num': 36, 'dish': 'おおぐいポテトサラダ', 'energy': 5040},
        {'ingredients': {'げきからハーブ': 17, 'あんみんトマト': 8, 'あったかジンジャー': 10}, 'num': 35, 'dish': 'オーバーヒートサラダ', 'energy': 5225},
        {'ingredients': {'あじわいキノコ': 17, 'あんみんトマト': 8, 'ピュアなオイル': 8}, 'num': 33, 'dish': 'キノコのほうしサラダ', 'energy': 5859},
        {'ingredients': {'ピュアなオイル': 15, 'おいしいシッポ': 10, 'げきからハーブ': 10}, 'num': 35, 'dish': 'ヤドンのしっぽペッパーサラダ', 'energy': 8169},
        {'ingredients': {'ふといながねぎ': 15, 'ワカクサ大豆': 15, 'あじわいキノコ': 12, 'あったかジンジャー': 11}, 'num': 53, 'dish': 'にんじゃサラダ', 'energy': 10095},
    ]

    # デザート・ドリンクのレシピ
    drink_recipes = [
        {'ingredients': {'モーモーミルク': 7}, 'num': 7, 'dish': 'モーモーホットミルク', 'energy': 727},
        {'ingredients': {'とくせんリンゴ': 8}, 'num': 8, 'dish': 'とくせんリンゴジュース', 'energy': 763},
        {'ingredients': {'あまいミツ': 9}, 'num': 9, 'dish': 'クラフトサイコソーダ', 'energy': 964},
        {'ingredients': {'モーモーミルク': 4, 'とくせんリンゴ': 12}, 'num': 16, 'dish': 'ねがいごとアップルパイ', 'energy': 1634},
        {'ingredients': {'モーモーミルク': 5, 'ほっこりポテト': 9}, 'num': 14, 'dish': 'じゅくせいスイートポテト', 'energy': 1783},
        {'ingredients': {'とくせんリンゴ': 7, 'あったかジンジャー': 9}, 'num': 16, 'dish': 'ひのこのジンジャーティー', 'energy': 1788},
        {'ingredients': {'ワカクサ大豆': 7, 'とくせんエッグ': 8}, 'num': 15, 'dish': 'かるわざソイケーキ', 'energy': 1798},
        {'ingredients': {'とくせんリンゴ': 7, 'あんみんトマト': 9}, 'num': 16, 'dish': 'マイペースやさいジュース', 'energy': 1798},
        {'ingredients': {'モーモーミルク': 7, 'ピュアなオイル': 10, 'あまいミツ': 6}, 'num': 23, 'dish': 'おおきいマラサダ', 'energy': 2927},
        {'ingredients': {'ワカクサ大豆': 15, 'リラックスカカオ': 8}, 'num': 23, 'dish': 'はりきりプロテインスムージー', 'energy': 3168},
        {'ingredients': {'ワカクサ大豆': 6, 'リラックスカカオ': 7, 'ピュアなオイル': 9}, 'num': 22, 'dish': 'ちからもちソイドーナツ', 'energy': 3213},
        {'ingredients': {'リラックスカカオ': 8, 'モーモーミルク': 7, 'あまいミツ': 9}, 'num': 24, 'dish': 'あまいかおりチョコケーキ', 'energy': 3280},
        {'ingredients': {'リラックスカカオ': 8, 'モーモーミルク': 9, 'とくせんリンゴ': 11, 'あまいミツ': 7}, 'num': 35, 'dish': 'あくまのキッスフルーツオレ', 'energy': 4734},
        {'ingredients': {'リラックスカカオ': 5, 'とくせんエッグ': 4, 'あまいミツ': 14, 'あったかジンジャー': 12}, 'num': 35, 'dish': 'ふくつのジンジャークッキー', 'energy': 4921},
        {'ingredients': {'とくせんリンゴ': 15, 'あったかジンジャー': 11, 'あじわいキノコ': 9}, 'num': 35, 'dish': 'ネロリ博士のヒーリングティー', 'energy': 5065},
        {'ingredients': {'モーモーミルク': 10, 'とくせんリンゴ': 10, 'とくせんエッグ': 15, 'あまいミツ': 20}, 'num': 55, 'dish': 'プリンのプリンアラモード', 'energy': 7594},
    ]

    try:
        ingredients['ふといながねぎ'] = int(request.form.get('negi', 0, type=int))
        ingredients['あじわいキノコ'] = int(request.form.get('kinoko', 0, type=int))
        ingredients['とくせんエッグ'] = int(request.form.get('egg', 0, type=int))
        ingredients['ほっこりポテト'] = int(request.form.get('potato', 0, type=int))
        ingredients['とくせんリンゴ'] = int(request.form.get('apple', 0, type=int))
        ingredients['げきからハーブ'] = int(request.form.get('herb', 0, type=int))
        ingredients['マメミート'] = int(request.form.get('meet', 0, type=int))
        ingredients['モーモーミルク'] = int(request.form.get('milk', 0, type=int))
        ingredients['あまいミツ'] = int(request.form.get('mitsu', 0, type=int))
        ingredients['ピュアなオイル'] = int(request.form.get('oil', 0, type=int))
        ingredients['あったかジンジャー'] = int(request.form.get('ginger', 0, type=int))
        ingredients['あんみんトマト'] = int(request.form.get('tomato', 0, type=int))
        ingredients['リラックスカカオ'] = int(request.form.get('cacao', 0, type=int))
        ingredients['おいしいシッポ'] = int(request.form.get('tail', 0, type=int))
        ingredients['ワカクサ大豆'] = int(request.form.get('beans', 0, type=int))

        variety = int(request.form.get('variety'))
        pot_size = int(request.form.get('pot_size'))

        max_energy = 0
        best_recipe = None
        
        if variety == 1:
            for curry_recipe in curry_recipes:
                can_cook = True
                for ingredient, required_count in curry_recipe['ingredients'].items():
                    if ingredients[ingredient] < required_count:
                        can_cook = False
                        break
                if can_cook:
                    energy = curry_recipe['energy']
                    if energy > max_energy and curry_recipe['num'] <= pot_size:
                        max_energy = energy
                        best_recipe = curry_recipe

        elif variety == 2:
            for salad_recipe in salad_recipes:
                can_cook = True
                for ingredient, required_count in salad_recipe['ingredients'].items():
                    if ingredients[ingredient] < required_count:
                        can_cook = False
                        break
                if can_cook:
                    energy = salad_recipe['energy']
                    if energy > max_energy and salad_recipe['num'] <= pot_size:
                        max_energy = energy
                        best_recipe = salad_recipe
                        
        elif variety == 3:
            for drink_recipe in drink_recipes:
                can_cook = True
                for ingredient, required_count in drink_recipe['ingredients'].items():
                    if ingredients[ingredient] < required_count:
                        can_cook = False
                        break
                if can_cook:
                    energy = drink_recipe['energy']
                    if energy > max_energy and drink_recipe['num'] <= pot_size:
                        max_energy = energy
                        best_recipe = drink_recipe

        return render_template('result.html', best_recipe=best_recipe)
    
    except ValueError:
        return '無効な入力です。整数を入力してください。'

if __name__ == '__main__':
    app.run()
