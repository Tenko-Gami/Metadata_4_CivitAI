def output_to_html(file, extracted_data, file_name):
    html = f"""
<!DOCTYPE html>
<html>
<body>

<h2>{file_name} :</h2>
    <ul>
      <li>Image Size : {extracted_data["width"]}x{extracted_data["height"]}</li>
      <li>Chekpoint : {extracted_data["ckpt_name"]} ({extracted_data["ckpt_hash"]})</li>
      <li>Loras : {extracted_data["lora_hashes"]}</li>
      <li>positive_prompt : {extracted_data["positive_prompt"]}</li>
      <li>negative_prompt : {extracted_data["negative_prompt"]}</li>
      <li>cfg : {extracted_data["cfg"]}</li>
      <li>sampler_name : {extracted_data["sampler_name"]}</li>
      <li>scheduler : {extracted_data["scheduler"]}</li>
      <li>steps : {extracted_data["steps"]}</li>
      <li>seed : {extracted_data["seed"]}</li>
    </ul>

</body>
</html>
    """

    file.write(html)
