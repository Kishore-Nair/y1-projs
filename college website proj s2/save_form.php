<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fullname = $_POST['fullname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $gender = $_POST['gender'];
    $dob = $_POST['dob'];
    $course = $_POST['course'];
    $password = $_POST['password'];

    // Handle file upload
    $file = $_FILES['file'];
    $uploadDirectory = 'uploads/';
    $uploadFilePath = $uploadDirectory . basename($file['name']);
    
    // Ensure the upload directory exists
    if (!is_dir($uploadDirectory)) {
        mkdir($uploadDirectory, 0755, true);
    }

    // Move uploaded file to the upload directory
    if (move_uploaded_file($file['tmp_name'], $uploadFilePath)) {
        $filePath = $uploadFilePath;
    } else {
        echo "Error uploading file.";
        exit;
    }

    // Save form data to a text file
    $data = "Full Name: $fullname\nEmail: $email\nPhone: $phone\nGender: $gender\nDate of Birth: $dob\nCourse: $course\nFile Path: $filePath\nPassword: $password\n\n";
    file_put_contents('submissions.txt', $data, FILE_APPEND);

    // Redirect to a thank you page
    header('Location: thanks.html');
    exit;
} else {
    echo "Invalid request method.";
}
?>
