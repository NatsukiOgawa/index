function search(idname){
  // value値を取得する
  var result = document.getElementById(idname).value;
  // 最終的な処理を記述する
  // これ以降に、文字列を扱う検索システムを記述する
  if (result.indexOf('あ')!==-1 || result.indexOf('い')!==-1 || result.indexOf('う')!==-1 || result.indexOf('え')!==-1　|| result.indexOf('お')!==-1){
    alert("「あ行」だよ！");
    }
  }

  function colorChange(idname){
    var element = document.getElementById(idname);
    element.style.background = '#ff0000';  //背景色を赤にする
    }
