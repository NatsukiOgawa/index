<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/Users/natsukiogawa/Desktop/sample-html/sample.css">
    <script type="text/javascript" src="/Users/natsukiogawa/Desktop/sample-html/sample.js">

    </script>
    <title></title>
  </head>
  <body>
    <?php

  define('APPID',        'dj00aiZpPU1tVGZnNnM2RDFCaSZzPWNvbnN1bWVyc2VjcmV0Jng9ZDQ-');
  define('SECRET',       '0qkN5cO0uT5yQMpDj2O9krrI9APGN3w0c4f1NY8P');
  define('CALLBACK_URL', '＜コールバックURL＞');
  define('TOKEN_URL',    'https://auth.login.yahoo.co.jp/yconnect/v1/token');

  $header = [
      'Content-Type: application/x-www-form-urlencoded',
      'Authorization: Basic ' . base64_encode(APPID . ':' . SECRET),
  ];

  $param = array(
      'code'         => ＜認可コード（code）＞,
      'grant_type'   => 'authorization_code',
      'redirect_uri' => CALLBACK_URL,
  );

  // 任意でオプションの追加をしてください。
  $ch = curl_init(TOKEN_URL);
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST,  'POST');
  curl_setopt($ch, CURLOPT_HTTPHEADER,     $header);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_POST,           true);
  curl_setopt($ch, CURLOPT_POSTFIELDS,     http_build_query($param));

  $response = curl_exec($ch);
  curl_close($ch);

  // 任意でレスポンスデータの判定処理を追加してください。
  $token = json_decode($response, true);

  // 実行した結果は下記に別枠で記載しております。
  var_dump($token);

?>
  </body>
</html>
