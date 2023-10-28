async function refreshMostPopular() {
    const Books = await loadBooks();
    let HtmlString = ``;
    let isLoggedIn = await isUserLoggedIn() === "true"; 
    let i = 0;
    for (let book of Books) {
        if (!isLoggedIn && i++ == 8) {
          break;
        }

        let bookURL = `{% url 'landing_page:get_review_data' 0 %}`.replace("0", book.pk)
        let year = book.fields["year"]
        let publisher = book.fields["publisher"]
        let imageURL = book.fields["image_url_l"]
        let bookTitle = book.fields["title"]
        let bookAuthor = book.fields["author"]
        let avgRating = book.fields["total_ratings"] / book.fields["total_reviews"]
        let totalReviews = book.fields["total_reviews"]
        totalReviews = (totalReviews > 1000) ? (totalReviews / 1000).toFixed(1) + "K" : 
          (totalReviews > 1000000) ? (totalReviews / 1000000).toFixed(1) + "M" : totalReviews

        if (isNaN(avgRating)) {
            avgRating = 0
        }

        avgRating = avgRating.toFixed(1)
        bookTitle = (bookTitle.length > 25) ? bookTitle.substring(0, 25) + "..." : bookTitle
        bookAuthor = (bookAuthor.length > 20) ? bookAuthor.substring(0, 20) + "..." : bookAuthor
        
        if (isLoggedIn){
          HtmlString += `
          <div class="col-lg-3 col-sm-6" id="book-item" year="${year}" publisher="${publisher}">
              <div class="item">
                <a href=${bookURL}>
                    <img class="img-fluid" src="${imageURL}" alt="${bookTitle}">
                </a>
                <h4>${bookTitle}<br><span>${bookAuthor}</span></h4>
                <ul class="d-flex flex-row text-left justify-content-between align-items-center">
                  <li class="d-flex align-items-start"><i class="fa fa-star"></i>${avgRating}</li>
                  <li class="d-flex"><i class="fa fa-users"></i>${totalReviews}</li>
                </ul>
                <div class="d-flex justify-content-center">
                  <div class="main-border-button" id="bookmark-link" style="margin: 15px 0 0 0;">
                    <a href="#"><i id="bookmark-logo" class="fa fa-bookmark" style="color: red;"></i> 
                      Add to Bookmark
                    </a>
                  </div>
                </div>
              </div>
          </div>`
        } else {
          HtmlString += `
          <div class="col-lg-3 col-sm-6" id="book-item" year="${year}">
              <div class="item">
                <a href=${bookURL}>
                    <img class="img-fluid" src="${imageURL}" alt="${bookTitle}">
                </a>
                <h4>${bookTitle}<br><span>${bookAuthor}</span></h4>
                <ul class="d-flex flex-row text-left justify-content-between align-items-center">
                  <li class="d-flex align-items-start"><i class="fa fa-star"></i>${avgRating}</li>
                  <li class="d-flex"><i class="fa fa-users"></i>${totalReviews}</li>
                </ul>
              </div>
          </div>`
        }
    }
    
    document.getElementById("most-popular-content").innerHTML += HtmlString + 
        `<div class="col-lg-12">
            <div class="main-button">
                <a href="" id="discover-more">Discover More</a>
            </div>
          </div>`;

    document.querySelectorAll("#bookmark-link").forEach((element) => {
      element.addEventListener("click", (event) => {
        event.preventDefault();
        let bookmarkLogo = element.querySelector("a");
        if (bookmarkLogo.querySelector("#bookmark-logo").style.color == "red") {
          bookmarkLogo.innerHTML = `<i id="bookmark-logo" class="fa fa-bookmark" style="color: green;"></i> ` + "Bookmarked";
          bookmarkLogo.style.color = "green";
        } else {
          bookmarkLogo.innerHTML = `<i id="bookmark-logo" class="fa fa-bookmark" style="color: red;"></i> ` + "Add to Bookmark";
          bookmarkLogo.style.color = "";
        }
      });
    });

    if (!isLoggedIn) {
      document.getElementById("login-logout").innerHTML = "Login";
      document.getElementById("login-logout").setAttribute("href", "{% url 'authentication:login' %}");
    } else {
      document.getElementById("login-logout").innerHTML = "Logout";
      document.getElementById("login-logout").setAttribute("href", "{% url 'authentication:logout' %}");
    }

    document.getElementById("discover-more").innerHTML = (isLoggedIn) ? "Back to Top" : "Login to Discover More";
    document.getElementById("discover-more").setAttribute("href", (isLoggedIn) ? "#most-popular-content" : "{% url 'authentication:login' %}");
} 

async function refreshFAQ() {
    const FAQ = await loadFAQ();
    const isLoggedIn = await isUserLoggedIn() === "true";

    let HtmlString = `
      <div class="col-lg-12">
        <div class="heading-section">
          <h4><em>Need Some Help?</em> Ask Us Now!</h4>
        </div>
      </div>
    `;
    
    if (isLoggedIn){
      for (let faq of FAQ) {
        let question = faq.fields["question"];
        let answer = faq.fields["answer"];
        HtmlString += `
          <div class="col-lg-12">
            <div class="faq-item">
              <h4>${question}</h4>
              <p>${answer}</p>
            </div>
          </div>
        `;
      }
    } else {
      HtmlString += `
        <div class="col-lg-12">
          <div class="faq-item">
            <h4>Login to view FAQ</h4>
          </div>
        </div>
      `;
    }

    HtmlString += `
          <div class="col-lg-12">
            <div class="main-button">
              <a href="profile.html">View All My Reviews</a>
            </div>
          </div>
    `

    document.getElementById("user-faq").innerHTML =  HtmlString;
}

function handleSearch() {
    let searchBy = document.getElementById('searchBy').value;
    let searchKeyword = document.getElementById('searchText').value.trim();
    let bookItems = document.querySelectorAll('.item');
    let HtmlString = ""
    
    // Loop through book items and show/hide based on search criteria and keyword
    document.querySelectorAll("#book-item").forEach(book => {
      if (searchBy === "title") {
        if (book.querySelector("h4").childNodes[0].textContent.toLowerCase().includes(searchKeyword.toLowerCase())) {
          if (searchKeyword == "clar"){
            console.log(book.querySelector("h4").innerHTML)
          }
          book.style.display = "block";
        } else {
          book.style.display = "none";
        }
      } else if (searchBy === "author") {
        if (book.querySelector("h4 span").childNodes[0].textContent.toLowerCase().includes(searchKeyword.toLowerCase())) {
          book.style.display = "block";
        } else {
          book.style.display = "none";
        }
      } else if (searchBy === "year") {
        if (book.getAttribute("year") == searchKeyword) {
          book.style.display = "block";
        } else {
          book.style.display = "none";
        }
      } else if (searchBy === "publisher") {
        if (book.getAttribute("publisher").toLowerCase().includes(searchKeyword.toLowerCase())) {
          book.style.display = "block";
        } else {
          book.style.display = "none";
        }
      }
    })
}


refreshMostPopular();
refreshFAQ();

document.getElementById('search').addEventListener('submit', function (event) {
event.preventDefault();
handleSearch();
});

let searchByDropdown = document.getElementById('searchBy');
let searchTextInput = document.getElementById('searchText');

searchByDropdown.addEventListener('change', handleSearch);
searchTextInput.addEventListener('input', handleSearch);