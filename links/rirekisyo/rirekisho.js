function name_furigana_contents() {
  var x = document.getElementById("name_furigana_textarea").value;
  document.getElementById("name_furigana").textContent = x;
}

function ShowLength_name_furigana( header ) {
   document.getElementById("name_furigana_counter").innerHTML = header.length + "文字";
   ShowLength_works(header.length);
}

function namecontents() {
  var x = document.getElementById("name_textarea").value;
  document.getElementById("name").textContent = x;
}

function ShowLength_header( header ) {
   document.getElementById("name_counter").innerHTML = header.length + "文字";
   ShowLength_works(header.length);

}

function seinengappicontents() {
  var x = document.getElementById("seinengappi_textarea").value;
  document.getElementById("seinengappi").textContent = x;
}

function ShowLength_header( header ) {
   document.getElementById("seinengappi_counter").innerHTML = header.length + "文字";
   ShowLength_works(header.length);

}

function jusho_furiganacontents() {
  var x = document.getElementById("jusho_furigana_textarea").value;
  document.getElementById("jusho_furigana").textContent = x;
}

function ShowLength_header( header ) {
   document.getElementById("jusho_furigana_counter").innerHTML = header.length + "文字";
   ShowLength_works(header.length);

}

function yubincontents() {
  var x = document.getElementById("yubin_textarea").value;
  document.getElementById("yubin").textContent = x;
}

function ShowLength_header( header ) {
   document.getElementById("yubin_counter").innerHTML = header.length + "文字";
   ShowLength_works(header.length);

}

function jushocontents() {
  var x = document.getElementById("jusho_textarea").value;
  document.getElementById("jusho").textContent = x;
}

function ShowLength_header( header ) {
   document.getElementById("jusho_counter").innerHTML = header.length + "文字";
   ShowLength_works(header.length);

}
