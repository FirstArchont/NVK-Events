function loadExternalScript(url, callback) {
    const script = document.createElement('script');
    script.src = url;
    script.onload = callback; // Функция, которая выполнится после загрузки
    document.head.appendChild(script);
}

loadExternalScript('https://telegram.org/js/telegram-web-app.js?57', function() {
    const tg = window.Telegram.WebApp;

    // Имя пользователя
    const firstName = tg.initDataUnsafe.user?.first_name;
    const lastName = tg.initDataUnsafe.user?.last_name;
    const username = tg.initDataUnsafe.user?.username;
    const id = tg.initDataUnsafe.user?.id;
    const photo_url = tg.initDataUnsafe.user?.photo_url;

    sendToDjango(id, username);

    document.getElementById("flname").textContent = `${firstName} ${lastName}`;
    document.getElementById("username").textContent = `@${username}`;
    document.getElementById("photo-profile").src = photo_url;

    function sendToDjango(id, username) {
        const url = window.location.pathname;  // URL вашего Django-обработчика

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                telegram_id: id,
                username: username,
                create_event: false,
            }),
        })
        .then(response => response.json())
        .then(data => {
            console.log("Success:", data);
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }
});

