const btn = document.getElementById('btn');
btn.addEventListener('click', () => {
    const value = document.getElementById('inp').value;
    fetch('/changeDatabase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({value: value})
    })
    .then(res => res.json())
    .then(data => document.getElementById('output').innerText = data.value);
});