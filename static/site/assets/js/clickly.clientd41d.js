console.log('clickly client loaded');
function isInFrame() {
  try {
    return window.self !== window.top;
  }
  catch (error) {
    console.error(error);
    return true;
  }
}

function isClicklyMessage(event) {
  return event && event.data && event.data.clickly;
}

function clicklyPostMessage(action, payload) {
  if (!action || !parent) {
    return;
  }

  top.postMessage(Object.assign({}, payload || {}, {action: action, clickly: true}), '*');
}

function onMessage(action, callback) {
  if (!action || !parent) {
    return;
  }

  window.addEventListener('message', function (event) {
    if (!isClicklyMessage(event)) {
      return;
    }

    if (!event.data.action || event.data.action !== action) {
      return;
    }

    callback(event.data);
  });
}

function innerGetPageTypeMonitextTemporary() {
  if (window.location.pathname === '/') return 'home';
  else if (document.querySelectorAll('.subcategoryName').length > 0) return 'category';
  else if (document.querySelectorAll('.product-grid').length > 0 && window.location.pathname.split('/').length > 3) return 'products';
  else if (document.querySelectorAll('input[name="product_id"]').length > 0) return 'product';
  else return 'other';
}

function innerGetPageType() {
  if (window.location.hostname === 'monitex.com.ua') {
    return innerGetPageTypeMonitextTemporary();
  }
  return window.location.pathname === '/' ? 'home' : 'other';
}

function injectStylesheet() {
  const style = document.createElement('style');
  const styles = [
    'body {transform-origin: 0 0;}',
    'body.capture *:hover {outline: 2px solid blue}',
    '.clicklyhighlight {outline: 2px solid red;box-shadow:inset 0 0 0 2px red}'
  ];
  style.innerText = styles.join('\n');
  document.head.appendChild(style);
}

function getNodeSelectorString(node) {
  return node.tagName.toLowerCase() + (node.id ? '#' + node.id : '') + (!!node.className ? '.' + node.className.trim().replace(/\s+/g, '.') : '');
}

function traverseUp(node) {
  const items = [];
  do {
    items.push(node);
    node = node.parentNode;
  } while (node && ['html', 'body'].indexOf(node.tagName.toLowerCase()) === -1);
  return items.reverse();
}

function getNodeSelector(node) {
  return traverseUp(node).map(getNodeSelectorString).join(' > ');
}

function getNodeText(node) {
  const txt = node && node.innerText.trim() || node.getAttribute('alt') || node.getAttribute('title') || node.getAttribute('id') || node.getAttribute('name') || node.getAttribute('placeholder') || node && node.value || '';
  return txt.length > 250 ? txt.substring(0, 247) + '...' : txt;
}

function clearHighlight() {
  document.querySelectorAll('.clicklyhighlight').forEach(function (el) {
    el.classList.remove('clicklyhighlight');
  });
}

function onClick(event) {
  event.preventDefault();
  event.stopPropagation();
  if (event.type !== 'click') return;
  clearHighlight();
  clicklyPostMessage('click', {
    ec: window.location.toString(),
    ea: getNodeSelector(event.target),
    el: getNodeText(event.target),
    cd4: typeof window['clicklyGetPageType'] !== 'undefined' ? window['clicklyGetPageType']() : innerGetPageType()
  })
}

function buildQueryString(obj) {
  return Object.keys(obj).map(function (k) {
    return k + '=' + encodeURIComponent(obj[k]);
  }).join('&');
}


var tid = document.querySelector('script[data-clickly-tid]').getAttribute('data-clickly-tid');
var cid = parseInt((window.document.cookie.match(/_ga=GA\d\.\d\.(\d+)/) || ['0']).pop()) || '';
var debug = !!localStorage.getItem('debug');

function collector(event) {
  var data = {
    v: 1,
    tid: tid,
    cid: cid,
    t: 'event',
    cd1: cid,
    cd2: Date.now(),
    cd3: Date.now() + '.' + Math.random().toString(36).substring(5),
    cd4: typeof window['clicklyGetPageType'] !== 'undefined' ? window['clicklyGetPageType']() : innerGetPageType(),
    ec: window.location.toString(),
    ea: event ? getNodeSelector(event.target) : 'view',
    el: event ? getNodeText(event.target) : document.title
  };

  var url = 'https://www.google-analytics.com/collect?' + buildQueryString(data);
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url);
  } else {
    fetch(url);
  }
  if (debug) {
    console.table([data]);
  }
}

console.log('clickly isInFrame', isInFrame());
if (isInFrame()) {
  injectStylesheet();

  console.log('sending navigated message');
  clicklyPostMessage('navigated', {
    ec: window.location.toString(),
    el: document.title,
    cd4: typeof window['clicklyGetPageType'] !== 'undefined' ? window['clicklyGetPageType']() : innerGetPageType()
  });

  onMessage('zoom', function (payload) {
    document.body.style.transform = 'scale(' + (payload.value || '1') + ')';
  });

  onMessage('highlight', function (payload) {
    clearHighlight();

    document.querySelectorAll(payload.selector).forEach(function (el) {
      return el.classList.add('clicklyhighlight');
    });
  });

  onMessage('emulate', function (payload) {
    var el = document.querySelector(payload.selector);

    if (el) {
      onClick({
        type: 'click',
        target: el,
        preventDefault: function () {
        },
        stopPropagation: function () {
        }
      });
    } else {
      console.log('emulate selector not found', payload.selector);
    }
  });

  onMessage('capture', function () {
    document.addEventListener('mousedown', onClick, true);
    document.addEventListener('mouseup', onClick, true);
    document.addEventListener('click', onClick, true);
    document.body.classList.add('capture');
  });

  onMessage('release', function () {
    document.removeEventListener('mousedown', onClick, true);
    document.removeEventListener('mouseup', onClick, true);
    document.removeEventListener('click', onClick, true);
    document.body.classList.remove('capture');
  });
} else {
  document.body.addEventListener('mousedown', collector, true);
  collector();
}


