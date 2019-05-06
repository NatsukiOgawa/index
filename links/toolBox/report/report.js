// Length START

function ShowLength_header( header ) {
   document.getElementById("header-counter").innerHTML = header.length + "文字";
   ShowLength_works(header.length);
}

function ShowLength_main( main ) {
   document.getElementById("main-counter").innerHTML = main.length + "文字";
   ShowLength_works(main.length);
}

function ShowLength_footer( footer ) {
   document.getElementById("footer-counter").innerHTML = footer.length + "文字";
   ShowLength_works(footer.length);
}

function ShowLength_works( works ) {
   works = header.length + main.length + footer.length;
   document.getElementById("works-counter").innerHTML = works.length + "文字";
}

// Length FINISH


// Cntents START

function headercontents() {
  var x = document.getElementById("header-textarea").value;
  document.getElementById("label-header").textContent = x;
}

function maincontents() {
  var y = document.getElementById("main-textarea").value;
  document.getElementById("label-main").textContent = y;
}

function footercontents() {
  var z = document.getElementById("footer-textarea").value;
  document.getElementById("label-footer").textContent = z;
}

function author_contents() {
  var author = document.getElementById("author_input").value;
  document.getElementById("author").textContent = author;
}

function year_contents() {
  var year = document.getElementById("year_input").value;
  document.getElementById("year").innerHTML = "(" + year + ")";
}

function page_title_contents() {
  var page_title = document.getElementById("page_title_input").value;
  document.getElementById("page_title").innerHTML = "「" + page_title + "」,";
}

function url_contents() {
  var url = document.getElementById("url_input").value;
  document.getElementById("url").innerHTML = "&lt;" + url + "&gt;";
}

function access_contents() {
  var access = document.getElementById("access_input").value;
  document.getElementById("access").innerHTML = "「" + access + " アクセス」";
}

// Contents FINISH
