function setCookie(key, value, expires = '', domain = window.location.hostname, path = '/') {
    const time = expires ? new Date(expires) : expires;
    console.log(time);
    const cookie = `${key}=${value}; expires=${time}; domain=${domain}; path=${path}`;
    document.cookie = cookie;
}

function cookieKeyGetValue(key) {
    const Cookie = document.cookie
    const cookieList = Cookie.split('; ')
    const cookieKeyList = cookieList.map(item => {
        return item.split('=')[0]
    })
    const index = cookieKeyList.indexOf(key)
    return cookieList[index].split('=')[1]
}