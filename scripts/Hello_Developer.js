class Developer {
  constructor({ name, age, language }) {
    this.name = name;
    this.age = age;
    this.language = language;
  }
  displayInfo() {
    return `${this.name} is a ${this.age} year old ${this.language} developer`;
  }
}

let dev = new Developer({
  name: 'Brad Beltowski',
  age: 34,
  language: 'Javascript',
});
dev.displayInfo(); // result: Brad Beltowski is a 34 year old Javascript developer
