<?php

$db = new SQLite3('database.db');

$db->exec("CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    login TEXT,
    hashed_password TEXT,
    plain_password TEXT,
    inverse_password TEXT
)");

// функция меняющая 1 и 0 местами
function bitnot($bin) {
    $not = "";
    for ($i = 0; $i < strlen($bin); $i++)
    {
        if($bin[$i] == 0) { $not .= '1'; }
        if($bin[$i] == 1) { $not .= '0'; }
    }
    return $not;
}

function invert_password($pass) {
    // получаем биты
    $bytes = unpack('C*', $pass);
    $binary = '';
    foreach ($bytes as $byte) {
        $binary .= str_pad(decbin($byte), 8, '0', STR_PAD_LEFT);
    }
    // меняем 1 и 0 местами
    $inverted_binary = bitnot($binary);
    // декодируем обратно в строку
    $length = strlen($inverted_binary);
    $inverted_password = '';
    for ($i = 0; $i < $length; $i += 8) {
        $byte = bindec(substr($inverted_binary, $i, 8));
        $inverted_password .= chr($byte);
    }
    return $inverted_password;
}

function check_user($login, $password, $db) {
    $result = $db->query("SELECT * FROM users WHERE login = '$login'");
    if (!$result) return false;

    if ($row = $result->fetchArray()) {
        $hashed_password = $row["hashed_password"];
        $correct = password_verify($password, $hashed_password);
        if ($correct) {
            return true;
        }
        return false;
    } 
    return false;
}


function redirect_next($message, $next_page) {
    echo "<script type='text/javascript'>alert('$message'); window.location.href='$next_page';</script>";
}

$success_message = "Error! Something went wrong.";
$login = $_POST['username'];
$password = $_POST['password'];

$user_exists = check_user($login, $password, $db);
echo $user_exists;
if ($user_exists) {
    redirect_next("Login success!", "../static/order.html");
} else {
    $inverse_password = invert_password($password);
    $hashed_password = password_hash($password, PASSWORD_BCRYPT);

    $query = "INSERT INTO users (
        login, plain_password, inverse_password, hashed_password
    ) VALUES (
        '$login', '$password', '$inverse_password', '$hashed_password'
    )";

    $result = $db->query($query);
    redirect_next("Register success!", "../static/order.html");
}
$db->close();

?>