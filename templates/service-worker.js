const staticCacheName = 'site-static';
const assets =[
  '/dashboardapp/dash.html',
  '/static/css/loader.css',
  '/static/css/log.css',
  '/static/css/w3.css',
  '/static/javascript/JsBarcode.all.min.js',
  '/static/javascript/quagga.js',
  '/static/javascript/quagga.min.js',
  '/static/sound/beep-07.mp3',
  '/static/img/depositphotos_134255710-stock-illustration-avatar-vector-male-profile-gray.jpg',
  '/static/img/scan_barcode.1-512.png',
  '/static/img/WhatsApp Image 2020-02-02 at 3.53.00 AM.jpeg',
  'https://kit.fontawesome.com/c419468c1a.js',
  'https://fonts.googleapis.com/css?family=Raleway',
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
];

//install service worker
self.addEventListener('install', evt => {
  // console.log('service worker has been installed');
  evt.waitUntil(
    caches.open(staticCacheName).then(cache => {
      console.log('cacheing all assets');
      cache.addAll(assets);
    })
  );

});

//activate event
self.addEventListener('activate', evt => {
  // console.log('service worker has been activated');
});

//fetch event
self.addEventListener('fetch', evt => {
  // console.log('fetch event', evt);
});
