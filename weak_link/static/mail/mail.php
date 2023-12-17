<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    
    $to = 'director@example.com';
    $subject = 'Данные анализатора';
    
    $message = '<p><strong>Руководитель:</strong> ' . $data['director'] . '</p>';
    $message .= '<p><strong>Отдел:</strong> ' . $data['department'] . '</p>';
    $message .= '<p><strong>Комментарий:</strong> ' . $data['message'] . '</p>';
    
    $message .= '<table border="1">
                    <tr>
                        <th>Имя сотрудника</th>
                        <th>Вероятность увольнения</th>
                        <th>Департамент</th>
                        <th>Руководитель</th>
                        <th>Дата</th>
                    </tr>';
    
    foreach ($data['tableData'] as $row) {
        $message .= '<tr>
                        <td>' . $row['name'] . '</td>
                        <td>' . $row['probability'] . '</td>
                        <td>' . $row['department'] . '</td>
                        <td>' . $row['director'] . '</td>
                        <td>' . $row['date'] . '</td>
                    </tr>';
    }
    
    $message .= '</table>';
    
    $headers = "Content-type: text/html; charset=utf-8\r\n";
    $headers .= "From: webmaster@example.com\r\n";
    
    mail($to, $subject, $message, $headers);
    
    http_response_code(200);
} else {
    http_response_code(400);
}
?>