**Аторизация**
----

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
 
**Создание/Изменение/Удаление опросов**
______

* **URL**
  * Для создания

    /create/quiz/
  
  * Для изменения
  
    /edit/quiz/pk/
  
  * Для удаления

    /delete/quiz/pk/
  
  PK - номер опроса
  
* **Cоздание**
  * **Метод:**

      `POST`
      
  * **Параметры** 
   
      **Обязательно**
      
     `title=[string]`
     
     `description=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'title' : 'string', 'description' : "string" }`
    
* **Изменение**
  
    * **Метод**
        
        `PUT`
        
    * **Параметры** 
   
      **Обязательно**
      
     `title=[string]`
     
     `description=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'title' : 'string', 'description' : "string" }`

* **Удаление**
  
    * **Метод**
        
        `DELETE`
        
    * **Параметры** 
   
      **Обязательно**
      
     `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{}`
______
**Создание/Изменение/Удаление вопросов**
______

* **URL**
  * Для создания

    /create/question/
  
  * Для изменения
  
    /edit/question/pk/
  
  * Для удаления

    /delete/question/pk/
  
  PK - номер опроса
  
* **Cоздание**
  * **Метод:**

      `POST`
      
  * **Параметры** 
   
      **Обязательно**
      
     `question_type=[1, 2, 3]`
     
     `quiz_id=[int]`
     
     `text=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'question_type' : 'string', 'quiz_id' : 'string', 'text' : "string" }`
    
* **Изменение**
  
    * **Метод**
        
        `PUT`
        
    * **Параметры** 
   
      **Обязательно**
      
     `text=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'text' : 'string'}`

* **Удаление**
  
    * **Метод**
        
        `DELETE`
        
    * **Параметры** 
   
      **Обязательно**
      
     `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{}`
