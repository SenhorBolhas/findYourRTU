<?php
if(isset($_POST["submit"])) {
    $recipient="findyourrtu@gmail.com";
    $subject="Email from website";
    $sender=$_POST["client"];
    $senderEmail=$_POST["email"];
    $message=$_POST["message"];

    $mailBody="Name: $sender\nEmail: $senderEmail\n\n$message";
    echo $message; 
    $success = mail($recipient, $subject, $mailBody, "From: $sender <$senderEmail>");

   
}
?>