<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Игра 5x5 с Картинками</title>
    <style>
        /* Общие стили для страницы */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Высота экрана */
            background-color: #f0f0f0;
            border: 5px solid black; /* Черная рамка вокруг всего приложения */
            border-radius: 15px; /* Закругленные углы рамки */
            overflow: hidden; /* Запрещаем прокрутку */
            box-sizing: border-box;
            flex-direction: column; /* Для вертикального расположения */
        }

        /* Стили для заголовка */
        .header {
            text-align: center;
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            font-weight: bold;
            color: white;
            background-color: black;
            width: 100%;
            padding: 10px 0;
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
        }

        /* Контейнер для игрового поля */
        .game-container {
            display: grid;
            grid-template-columns: repeat(5, 60px); /* 5 ячеек по 60px */
            grid-template-rows: repeat(5, 60px); /* 5 ячеек по 60px */
            gap: 3mm; /* Расстояние между ячейками */
            justify-items: center;
            align-items: center;
            padding: 10px;
            background-color: white;
            border-radius: 10px; /* Закругленные углы игрового поля */
        }

        /* Стиль ячеек */
        .cell {
            width: 60px;
            height: 60px;
            background-color: #009688;
            border: 1px solid #00796b;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px; /* Размер текста */
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
            overflow: hidden;
        }

        /* Эффект на ховер */
        .cell:hover {
            background-color: #00796b;
        }

        /* Стили для изображений в ячейках */
        .cell img {
            width: 100%;
            height: 100%;
            object-fit: cover; /* Сохраняет пропорции изображения */
        }

        /* Стили для счетчика */
        .counter {
            font-family: 'Arial', sans-serif;
            font-size: 20px;
            color: white;
            background-color: #009688;
            padding: 5px;
            border-radius: 5px;
        }

        /* Черный фон с текстом "klawouns" */
        .footer {
            width: 100%;
            background-color: black;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 18px;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
        }

        /* Фон всего тела приложения */
        .app-container {
            background-color: black; /* Черный фон */
            width: 100%;
            padding: 20px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            flex-grow: 1;
        }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="header">
            Собрано:
            <br>
            <span id="counter" class="counter">0</span>
        </div>

        <div class="game-container">
            <!-- 25 ячеек для игрового поля -->
            <div class="cell" data-id="1"></div>
            <div class="cell" data-id="2"></div>
            <div class="cell" data-id="3"></div>
            <div class="cell" data-id="4"></div>
            <div class="cell" data-id="5"></div>
            <div class="cell" data-id="6"></div>
            <div class="cell" data-id="7"></div>
            <div class="cell" data-id="8"></div>
            <div class="cell" data-id="9"></div>
            <div class="cell" data-id="10"></div>
            <div class="cell" data-id="11"></div>
            <div class="cell" data-id="12"></div>
            <div class="cell" data-id="13"></div>
            <div class="cell" data-id="14"></div>
            <div class="cell" data-id="15"></div>
            <div class="cell" data-id="16"></div>
            <div class="cell" data-id="17"></div>
            <div class="cell" data-id="18"></div>
            <div class="cell" data-id="19"></div>
            <div class="cell" data-id="20"></div>
            <div class="cell" data-id="21"></div>
            <div class="cell" data-id="22"></div>
            <div class="cell" data-id="23"></div>
            <div class="cell" data-id="24"></div>
            <div class="cell" data-id="25"></div>
        </div>

        <!-- Футер с текстом "klawouns" -->
        <div class="footer">
            klawouns
        </div>
    </div>

    <script>
        // Ссылки на изображения
        const duckImage = 'https://bogatyr.club/uploads/posts/2023-03/1677914974_bogatyr-club-p-utka-s-otkritim-klyuvom-foni-krasivo-39.jpg';
        const petImage = 'https://sun9-48.userapi.com/s/v1/if2/GPYnUrxplkRMvHCcET1zjzw_o4kGDVHaMMQfUe-CXwSoJzix9t4r0Md71Mwzu2R9KuCfC_DPCGL6sgh6CvvYXuf3.jpg?quality=96&as=32x32,48x48,72x72,108x108,160x160,240x240,320x320';

        // Массив с номерами ячеек, которые будут показывать картинку с петухом
        const randomCells = [getRandomCell(), getRandomCell()];
        let score = 0;

        function getRandomCell() {
            return Math.floor(Math.random() * 25) + 1; // генерируем случайное число от 1 до 25
        }

        // Логика для открытия ячеек
        document.querySelectorAll('.cell').forEach(cell => {
            cell.addEventListener('click', function () {
                const cellId = parseInt(cell.dataset.id);

                // Если ячейка уже открыта, ничего не делаем
                if (cell.innerHTML !== '') return;

                // Проверка на случайные ячейки с изображением петуха
                if (randomCells.includes(cellId)) {
                    const img = document.createElement('img');
                    img.src = petImage;
                    cell.appendChild(img);
                } else {
                    const img = document.createElement('img');
                    img.src = duckImage;
                    cell.appendChild(img);
                }

                // Обновляем счетчик
                score++;
                document.getElementById('counter').textContent = score;
            });
        });
    </script>
</body>
</html>
