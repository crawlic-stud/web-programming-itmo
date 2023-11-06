<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $surname = $_POST["surname"];
    $email = $_POST["email"];
    $feedback = $_POST["feedback"];

    $one = $_POST["checkbox1"];
    $two = $_POST["checkbox2"];
    $three = $_POST["checkbox3"];

    echo $name  . '<br>';
    echo $surname . '<br>';
    echo $email . '<br>';
    echo $feedback . '<br>';

    if (isset($one)) {
        print("Вы выбрали первый чекбокс<br>");
    }

    if (isset($two)) {
        print("Вы выбрали второй чекбокс<br>");
    }

    if (isset($three)) {
        print("Вы выбрали третий чекбокс<br>");
    }

    $option = $_POST["option"];

    if (!isset($option)) {
        echo "Вы не поставили никакой оценки....... ну ладно...<br>";
    } else if ($option == "option1") {
        echo "Вы поставили лайк! УРА!<br>";
    } else {
        echo "Вы поставили дизлайк :(<br>";
    }
}
?>