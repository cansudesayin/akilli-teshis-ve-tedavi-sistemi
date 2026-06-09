document.addEventListener('DOMContentLoaded', function() {
  var t = document.createElement('div');
  t.id = 'global-toast';
  document.body.appendChild(t);
});

function showGlobalToast(msg, type) {
  var t = document.getElementById('global-toast');
  if(!t) return;
  t.innerHTML = (type === 'success' ? '✅ ' : '') + msg;
  t.className = type ? 'show ' + type : 'show';
  setTimeout(function(){ t.className = t.className.replace('show', '').trim(); }, 3500);
}

window.simBtn = function(event, msg, redirect) {
  if (event) event.preventDefault();
  var btn = event.currentTarget;
  if(btn.dataset.loading) return;
  btn.dataset.loading = 'true';
  
  var orig = btn.innerHTML;
  btn.style.width = btn.offsetWidth + 'px'; 
  btn.innerHTML = '<span class="spinner-btn"></span>';
  btn.style.opacity = '0.85';
  btn.style.pointerEvents = 'none';
  btn.style.justifyContent = 'center';

  setTimeout(function() {
    btn.innerHTML = orig;
    btn.style.width = '';
    btn.style.opacity = '1';
    btn.style.pointerEvents = 'auto';
    delete btn.dataset.loading;
    showGlobalToast(msg, 'success');
    if (redirect) setTimeout(function(){ window.location.href = redirect; }, 1500);
  }, 1200);
}
