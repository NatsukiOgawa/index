function search(idname){
  // value値を取得する
  var result = document.getElementById(idname).value;
  // 最終的な処理を記述する
  // これ以降に、文字列を扱う検索システムを記述する
  if (result.indexOf('html')!==-1 || result.indexOf('HTML')!==-1){
    window.open("/Users/natsukiogawa/Desktop/ホームページ/links/search/html_page.html", "null");
  }else
  if (result.indexOf('htlm')!==-1 || result.indexOf('hmtl')!==-1 || result.indexOf('hmlt')!==-1 || result.indexOf('HTLM')!==-1 || result.indexOf('HMTL')!==-1 || result.indexOf('HMLT')!==-1) {
    alert("もしかして「html」ですか？");
  }
  else {
    alert("ないよ〜。");
      }
  }
