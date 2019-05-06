function SortByCharCode() {
   // textareaの内容を改行で分割して配列に格納
   var targetArray = document.getElementById('sampleTargetLines').value.split("\n");
   // 文字コード順にソート
   var sortedArray = targetArray.sort();
   // ソート結果を書き戻す
   document.getElementById('sampleTargetLines').value = sortedArray.join("\n");
}
