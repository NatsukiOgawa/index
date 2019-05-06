function search(idname){
  // value値を取得する
  var result = document.getElementById(idname).value;
  // 最終的な処理を記述する
  // これ以降に、文字列を扱う検索システムを記述する
  if (result.indexOf('html')!==-1 || result.indexOf('HTML')!==-1){
    alert("「html」「HTML」だよ！");
  }else
  if (result.indexOf('css')!==-1 || result.indexOf('CSS')!==-1) {
    alert('「css」「CSS」だよ！');
  }else
  if (result.indexOf('javascript')!==-1 || result.indexOf('JAVASCRIPT')!==-1) {
    alert('「javascript」「JAVASCRIPT」だよ！');
  }else
  if (result.indexOf('jquery')!==-1 || result.indexOf('jQuery')!==-1) {
    alert('「jquery」「jQuery」だよ！');
  }else
  if (result.indexOf('java')!==-1 || result.indexOf('JAVA')!==-1) {
    alert('「java」「JAVA」だよ！');
    colorChange('list');
  }else{
    alert("なかった、、、。");
    }
  }

  function colorChange(idname){
  var element = document.getElementById(idname);
  element.style.background = '#ff0000';  //背景色を赤にする
  }
