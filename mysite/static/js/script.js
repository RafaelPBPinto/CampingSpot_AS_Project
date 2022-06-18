let navbarDiv = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
    if(document.body.scrollTop > 40 || document.documentElement.scrollTop > 40){
        navbarDiv.classList.add('navbar-cng');
    } else {
        navbarDiv.classList.remove('navbar-cng');
    }
});


const navbarCollapseDiv = document.getElementById('navbar-collapse');
const navbarShowBtn = document.getElementById('navbar-show-btn');
const navbarCloseBtn = document.getElementById('navbar-close-btn');
// show navbar
navbarShowBtn.addEventListener('click', () => {
    navbarCollapseDiv.classList.add('navbar-collapse-rmw');
});

// hide side bar
navbarCloseBtn.addEventListener('click', () => {
    navbarCollapseDiv.classList.remove('navbar-collapse-rmw');
});

document.addEventListener('click', (e) => {
    if(e.target.id != "navbar-collapse" && e.target.id != "navbar-show-btn" && e.target.parentElement.id != "navbar-show-btn"){
        navbarCollapseDiv.classList.remove('navbar-collapse-rmw');
    }
});

// stop transition and animatino during window resizing
let resizeTimer;
window.addEventListener('resize', () => {
    document.body.classList.add("resize-animation-stopper");
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        document.body.classList.remove("resize-animation-stopper");
    }, 400);
});

function setupSelector(selector) {
    selector.addEventListener('change', e => {
      console.log('changed', e.target.value)
    })
  
    selector.addEventListener('mousedown', e => {
      if(window.innerWidth >= 420) {// override look for non mobile
        e.preventDefault();
  
        const select = selector.children[0];
        const dropDown = document.createElement('ul');
        dropDown.className = "selector-options";
  
        [...select.children].forEach(option => {
          const dropDownOption = document.createElement('li');
          dropDownOption.textContent = option.textContent;
  
          dropDownOption.addEventListener('mousedown', (e) => {
            e.stopPropagation();
            select.value = option.value;
            selector.value = option.value;
            select.dispatchEvent(new Event('change'));
            selector.dispatchEvent(new Event('change'));
            dropDown.remove();
          });
  
          dropDown.appendChild(dropDownOption);   
        });
  
        selector.appendChild(dropDown);
  
        // handle click out
        document.addEventListener('click', (e) => {
          if(!selector.contains(e.target)) {
            dropDown.remove();
          }
        });
      }
    });
  }