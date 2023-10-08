<MyRoot>
    monetochka:monetochka
    predict: predict
    BoxLayout:
        orientation: "vertical"

        Label:
            text: "Жребий"
            font_size: 64
            color: 0.92, 0.45, 0

        Label:
            id: monetochka
            text: "_"
            font_size: 64
        Label:
            id: predict
            text: "_"
            font_size:64

        Button:
            text: "Подбросить монетку"
            font_size: 32
            size: 100, 50
            on_press: root.throw()
        Button:
            text: "Предсказать"
            font_size: 32
            size: 100, 50
            on_press: root.pred()
        Image:
            source: 'yyy.jpg'
            size: 44556, 555552
