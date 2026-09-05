import os
import urllib.request

OUTPUT_DIR = "audio"

FILES = {
    1: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213902_169a0405-92b4-4816-ac28-c5177d0b0201.mp3",
    2: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213919_255f5765-2cd0-4a47-afe4-29e5ce3947af.mp3",
    3: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213919_06596616-3ba1-4334-b182-aa89d7b523ce.mp3",
    4: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214040_c3d42369-5cbf-4c33-b1f6-619c916ef61d.mp3",
    5: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213919_3e419e16-390e-4417-8098-7f2ba85984b3.mp3",
    6: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213919_3773bb2a-6ffd-4147-9c69-6065b021071b.mp3",
    7: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214040_804bc2ae-c45d-4f7e-9e94-f6b7651806d1.mp3",
    8: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213919_531403ae-0909-4c21-b623-8448b330e12a.mp3",
    9: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213919_450b62a6-2c42-409e-b46f-5f50142888ce.mp3",
    10: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214040_156af0be-1972-4276-b0a1-eb31b6bed2bd.mp3",
    11: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214040_3f4d3467-59a2-4ba0-b045-10b1e233f522.mp3",
    12: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214050_3aa82b36-a4d0-4d23-b626-b2c7ed87eef3.mp3",
    13: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214050_8bedc348-2b92-419f-90e6-8516aa02b21c.mp3",
    14: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214050_ad02c902-aed0-40f9-bc92-da77517d09b2.mp3",
    15: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214050_e4bb531c-7208-4759-bc30-42b71fc71ffd.mp3",
    16: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214059_0f4f6d93-4ae7-4a4a-ad80-ed77a86e9a46.mp3",
    17: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213934_8d539975-f493-4a39-9c6d-4d8be0e2a9f5.mp3",
    18: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213934_fad465d9-39b8-4995-a544-f2f156fda825.mp3",
    19: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214059_ef80cda4-2b56-4ec3-b8c1-49aff44ccdd3.mp3",
    20: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213934_555580d1-ed12-4c01-b93c-ab9143985495.mp3",
    21: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213934_e08023a3-7266-41e1-acea-37f616882b56.mp3",
    22: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214059_388d19bf-2f7d-4516-9fe3-204749ce7e87.mp3",
    23: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214100_c172c6bf-b200-40db-acf4-e16b21aae3e4.mp3",
    24: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213934_312f9e39-f35b-4e61-a291-e43c873860b3.mp3",
    25: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_a9491646-3941-4035-9d73-6694dcbe59cc.mp3",
    26: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214106_1a89c3c1-52f1-41bf-9579-d3e1a924dbe7.mp3",
    27: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_c3f6df32-33c1-4279-bf25-dbf013e14a08.mp3",
    28: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_5d840a38-d65b-47ac-8b0f-4b392ce6c147.mp3",
    29: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_45ba2a30-f043-4b73-86a5-ce9e0e41b554.mp3",
    30: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_ff0572dd-b078-40dd-b717-11a1d2e10066.mp3",
    31: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214001_bb32fbd9-7030-4e53-b79b-5e035a505571.mp3",
    32: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_5a22f44f-3859-4e43-98d4-7367e10e3d43.mp3",
    33: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_e5da4ac8-109d-4a65-9575-09cba6d20ef8.mp3",
    34: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_3cad9ad1-d7b9-48ae-aaf0-35593fd92ea0.mp3",
    35: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_214001_d9ae1833-d829-48e4-bb11-1a504535b706.mp3",
    36: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213948_493b8db9-cae7-4ff8-9a15-e378e0ffaee3.mp3",
    37: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213953_6124d2ae-054a-4cc4-9be5-ea30e8226f23.mp3",
    38: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213953_148dbfe0-a232-47db-ae6c-ba984a839297.mp3",
    39: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213953_02691d89-727b-4ff8-b1d6-4c05b6f01fd2.mp3",
    40: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260905_213953_92dc87b6-8f8d-48ec-8877-e34f92ce634c.mp3",
}


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for image_num, url in sorted(FILES.items()):
        dest = os.path.join(OUTPUT_DIR, f"image_{image_num}.mp3")
        print(f"Downloading image_{image_num}.mp3 ...")
        urllib.request.urlretrieve(url, dest)
    print(f"Done. {len(FILES)} files saved to '{OUTPUT_DIR}/'.")


if __name__ == "__main__":
    main()
