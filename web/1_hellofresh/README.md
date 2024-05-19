# Hellofresh

In this exercise, you should simply recreate this Card:
![Form](./solution.png)

In this folder you will find the `index.html`, some assets and our evaluation
script. Please, edit the html file to recreate the card. You can import css in
any way you want. 

However, we have some restriction for this task:
- use the provided `hellofreshlogo.png` for the logo
- you **MUST** use flex-box to position the elements!
- set the attribute `id='logo'` to the hellofresh logo element
- set the attribute `id='title'` to element containing the upper section 
  ```
  DON'T MISS OUT
  Get 16 Free Meals
  Plus FREE Shipping
  ```
- set the attribute `id='form'` to the form element
- set the attribute `id='form-field'` to the email input element
- set the attribute `id='form-button'` to the submit button element

A few things about our evaluation script that runs in your browser:

It loosely checks the structure of your HTML. For example, it is not strict
about the exact color of an element or its border styles or even the text an element 
contains. We don't think that checking them is helpful to you as these simple
things to change. However, it will at least check that you have at least changed them, in
other words, that you have not left the default values. It may also have loose 
limits for some css properties e.g. such as the cards width which should not
be hard to change by you. 

However, the evaluation script is strict about the positioning of the elements. 
For example, we try to calculate the position of the logo to be precisely at the
center of your card.

The script will print all errors (such as missing ids, wrong positioning and other styling 
issues) to the developer console. Once your solution looks correct, refresh the page and
the script will prompt you to enter your email address. If not, your error is
in the console :). Once you have the solution, your generated individual key based 
on the email you entered can then be found in the developer console. 

*The script is probably not perfect, so if you think you have the correct
solution but the script does not recognize it, please join our next session and
discuss your solution with us! As always, if you have trouble with the task,
join our next session and we will help you!*
