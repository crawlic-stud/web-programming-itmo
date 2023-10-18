<?php
$db = new SQLite3('database.db');

$db->exec("CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    items TEXT,
    delivery_address TEXT,
    phone TEXT,
    email TEXT,
    comment TEXT
)");

$surname = $_POST['surname'];
$name = $_POST['name'];
$patronymic = $_POST['patronymic'];
$items = $_POST['items'];
$delivery_address = $_POST['delivery_address'];
$phone = $_POST['phone'];
$email = $_POST['email'];
$comment = $_POST['comment'];

$query = "INSERT INTO orders (
    surname, 
    name, 
    patronymic, 
    items, 
    delivery_address, 
    phone, 
    email, 
    comment
) VALUES (
    '$surname', 
    '$name', 
    '$patronymic', 
    '$items', 
    '$delivery_address', 
    '$phone', 
    '$email', 
    '$comment'
)";
$result = $db->exec($query);

$results = $db->query("SELECT * FROM orders");
while ($row = $results->fetchArray()) 
{
    var_dump($row);
}

$db->close();
?>


<?php 
if ($result) {
    ?>
    <div style="
        background-color: #28a745;
        color: white;
        padding: 10px;
        margin-bottom: 10px;
        width: 30%;
    ">
        <p>Success! Your action was completed successfully.</p>
    </div>

    <?php
} else {
    ?>
    <div style="
        background-color: #dc3545;
        color: white;
        padding: 10px;
        margin-bottom: 10px;
        width: 30%;
    ">
        <p>Error! Something went wrong. Please try again.</p>
    </div>
    <?php
}
?>

<br>
<button style="
    display: block;
    width: 30%;
    padding: 10px;
    color: white;
    background-color: #007BFF;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 5px;" 
    onclick="history.go(-1);"
>
OK
</button>


