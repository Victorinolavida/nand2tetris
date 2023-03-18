const FOLDER_FILES = "/Users/victorino.ruiz/Desktop/nand2tetris/projects/06/";
const fs = require("fs");
const { translate } = require("./code");

const args = process.argv.slice(2);
function main() {
  let FILE_PATH = "";

  if (args.length === 0) throw new Error("nombre del archivo vacio");

  const folders = [];
  fs.readdirSync(FOLDER_FILES).forEach((file) => {
    if (file.toString() !== "Assambler" && file.toString()!==".DS_Store") {
      folders.push(FOLDER_FILES + file + "/");
    }
  });

  if (folders.length === 0) throw new Error("la carpeta 06 esta vacia");

  while (folders.length !== 0) {
    const folder = folders.shift();
    fs.readdirSync(folder).forEach((file) => {
      if (args[0] == file) {
        FILE_PATH = folder + `${args[0]}`;
      }
    });
  }
  console.log(FILE_PATH);
  if (!FILE_PATH) throw new Error(`No se encontro el archivo ${args[0]}`);

  const data = fs.readFileSync(FILE_PATH, "utf8").split("\n").filter(Boolean);

  const code_machine = translate(data);

  //writing file
  
  fs.writeFileSync(`${args[0].replace('asm','hack')}`,code_machine.join("\n"));
  console.log(`file ${args[0].replace('asm','hack')} saved`)
}

try {
  main();
  
} catch (e) {
  console.error("Error: ", e.message);
}
