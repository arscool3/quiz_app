**Регистрация**
----

* **URL**

  /register/

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'username' : 'string', 'password' : "string" }`
    
 _____
**Аторизация**
----
Используйте username, который вам дали при регистрации 
Используйте его как `username` и как `password`
* **URL**

  /login/

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `username=[string]`
   `password=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'refresh' : 'string', 'access' : "string" }`
    
**Используйте ключ 'access' для авторизации**
 _____
**Просмотр всех вопросов активных опросов**
----

* **URL**

  /all/quiz/

* **Method:**

  `GET`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `cписок всех вопросов активных опросов`
    
 _____
**Просмотр всех вопросов конкретного опроса**
----

* **URL**

  /quiz/view/pk/
  
  pk - номер опроса

* **Method:**

  `GET`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `cписок всех вопросов конкретного опроса`
    
 _____
**Ответить на определенный вопрос**
----

* **URL**

  /answer/create/

* **Method:**

  `POST`
  
*  **Параметры**
    
   **Обязательно:**
 
   `question_id = [int]`
   `text = [string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** ` '{id' : 'int', 'text' : 'string', 'question_id' : 'int', 'user_id' : "int"}`
    
 _____
 **Просмотр всех ответов**
----

* **URL**

  /answer/view/

* **Method:**

  `GET`
  
*  **Параметры**
    
   **Обязательно:**
 
   `None`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** ` 'список всех ответов`
    
 _____
