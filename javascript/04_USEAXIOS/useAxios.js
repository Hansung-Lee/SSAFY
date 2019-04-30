const URL = 'https://dog.ceo/api/breeds/image/random'
/*
axios.get(URL) // AJAX CALL
    .then(response => {
        const imageUrl = response.data.message
        const imageBox = document.querySelector('#img-div')
        const image = document.createElement('img')
        image.src = imageUrl
        imageBox.appendChild(image)
    })
*/

// TODO: 위 코드를 async-await로 바꾸기
const getImage = async () => {
    const response = await axios.get(URL)
    const imageUrl = response.data.message
    const imageBox = document.querySelector('#img-div')
    const image = document.createElement('img')
    image.src = imageUrl
    imageBox.appendChild(image)
}
getImage()