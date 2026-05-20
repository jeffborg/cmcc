(function(){
  var nav=document.querySelector(".site-nav"),btn=document.querySelector(".hamburger");
  if(!btn||!nav)return;
  btn.addEventListener("click",function(){
    var open=nav.classList.toggle("nav-open");
    btn.setAttribute("aria-expanded",open?"true":"false");
  });
  var sc=false;
  window.addEventListener("scroll",function(){
    var s=window.scrollY>120;
    if(s!==sc){sc=s;document.body.classList.toggle("scrolled",s)}
  },{passive:true});
})();
