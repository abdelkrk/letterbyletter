import os
import urllib.request

OUTPUT_DIR = r"C:\Users\ASUS\Desktop\insurance_denial_audio"

FILES = {
    1: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122310_9443b36e-43b6-4345-aae5-a40f7f530f29.mp3",
    2: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122310_de30948c-9ff3-4814-a235-882e9b596e63.mp3",
    3: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122053_d8042b02-8445-4dfb-84f7-eb8286e9e6f7.mp3",
    4: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122310_ca6b8e21-c3eb-44f3-b708-0f6d734076c3.mp3",
    5: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122310_f3f78e3d-0f82-4858-bbff-cbf60f63b33b.mp3",
    6: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122325_537583e5-9f73-4c16-9770-5021332f72e2.mp3",
    7: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122053_084e4c8e-b5d8-4cc8-91e5-e1f8ac22fd57.mp3",
    8: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122326_8844810b-8f83-4a9e-8a9a-a32ecd10348c.mp3",
    9: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122053_4aea0107-4ea2-435c-bad1-1f8b9c45090e.mp3",
    10: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122053_8630ea66-2c1f-44eb-944b-c62ab558e14c.mp3",
    11: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122326_ff49ae45-292a-467e-8614-0d62d7ccf1a2.mp3",
    12: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122053_4f19449c-f32b-4806-a9bb-069633f20b63.mp3",
    13: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_ab18d127-d923-4070-a7be-a993f5b36606.mp3",
    14: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122325_8e4f05a4-3f86-4b43-8349-dcdb07e794e4.mp3",
    15: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_8e9e58ee-d0e8-4b19-a9fa-cdffdbb7bd87.mp3",
    16: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_0259bf1a-6a6a-45e0-bb84-37b6a3734978.mp3",
    17: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_2b361bc7-305f-4c10-af14-a04321dce3bb.mp3",
    18: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_af78c2f9-d4f0-4b84-a052-615cfb6e9aab.mp3",
    19: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122336_4d42022b-ce8e-4a82-b34c-dad38dd33c05.mp3",
    20: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_2d7b2fd3-d9f7-4278-8d09-937e57716c7c.mp3",
    21: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_ee7f47e9-4b80-4350-8c93-67bce75a26a7.mp3",
    22: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_459db50e-e8a0-4608-b11a-2a9d64e52775.mp3",
    23: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_421f63d6-754c-41ff-acab-f8a84da7a2cb.mp3",
    24: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122107_06c5beb9-c633-4567-b684-0893e4c3420e.mp3",
    25: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122119_9e2670bd-d005-41a3-a5d3-6666c3586c64.mp3",
    26: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122119_30f9eff7-a799-4a64-9330-0852a2ad4603.mp3",
    27: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122119_a8c86ed9-843e-4d86-b95d-5bf6f421d9b7.mp3",
    28: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122119_343b97f7-998d-47ea-ad31-898d57184d77.mp3",
    29: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122119_25e487fa-4858-4e1c-9686-9aa5e85f973d.mp3",
    30: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122336_f6f555ca-2589-4ba4-ae78-80bf17ac78a9.mp3",
    31: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122336_764a601e-0000-46b5-9972-bc26924adcd4.mp3",
    32: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122204_79564535-e03a-440d-92ed-70fb9cd70fce.mp3",
    33: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122119_ff3cef7d-3e9a-4edf-a936-fb025a1955f7.mp3",
    34: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122119_efea9ee6-c643-40d8-99ba-11c6f477cb21.mp3",
    35: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122336_bb415108-0c49-4882-8e3f-778b885f6629.mp3",
    36: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122119_d737485e-0bb6-419d-80a5-c4955e01440c.mp3",
    37: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_bbfadd21-23f3-4ba5-9baa-36513d0bf446.mp3",
    38: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_b9d6f6c9-523b-4983-a064-682726b4d0b0.mp3",
    39: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122346_433bf7bd-6a7e-4e00-a2fb-fb04c52944f7.mp3",
    40: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_680929ab-a708-47bb-aa4b-565cae41a9c0.mp3",
    41: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_a3152c43-b332-4c1b-bd22-4f19007d4aef.mp3",
    42: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_69b67d1b-452a-42d4-9676-d2d2414fb750.mp3",
    43: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_2986c2a8-d827-4ae2-af2c-2d339727aeaf.mp3",
    44: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_6ba20eea-614f-4aa7-98e9-eb1b4c2878d9.mp3",
    45: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_b510a0d6-8023-40b1-afb4-08699c50bc48.mp3",
    46: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122204_99e15d05-da79-447a-bb1e-68323c9e9a03.mp3",
    47: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122346_a032e865-cb97-492b-927e-90f42febb20b.mp3",
    48: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122134_44597240-87d2-4681-a38a-de190a5866c2.mp3",
    49: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122348_72d6ee20-8d31-48fe-b739-b2c6f845886d.mp3",
    50: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_c0e19884-8350-431d-bd80-9362131b3f59.mp3",
    51: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_9f7e6431-2afd-48d9-9349-649c761bab45.mp3",
    52: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_f5fecdf1-4b4d-4844-ba5b-3ad6ca9a0637.mp3",
    53: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_f6fe0ddf-65c6-4333-9279-b861f37916b5.mp3",
    54: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_f4abd042-db29-4ab0-9135-ac1653cc5bc1.mp3",
    55: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_9fb625e6-b9c9-4d24-be5d-5ca501841c9b.mp3",
    56: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_9c2d2386-623c-4698-9cbb-4aa9004226eb.mp3",
    57: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_db84b12d-182a-4aa7-98df-9e2795adcb46.mp3",
    58: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122348_b74bbd5a-c2f1-490d-aaee-d597d435371f.mp3",
    59: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_0d3bbac0-8581-458e-a4ca-c705f0229b4d.mp3",
    60: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122140_4ae60cb6-854e-4ccf-ba03-778337d89347.mp3",
    61: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122407_59deb327-62e5-4a4f-967b-7bdfcd3b841f.mp3",
    62: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122407_b0e9b4bd-4aea-4a8c-bd9b-b1c0abecffb4.mp3",
    63: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122407_9320127e-2c1b-4344-bad2-05c83be2eee4.mp3",
    64: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122149_673a1320-f7a6-4980-b482-b823c4e0a6f0.mp3",
    65: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122149_b6e2269f-1b91-4fb9-a440-293322b6db05.mp3",
    66: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122149_96aff9b2-08ad-4bd2-aa27-198f06a52cfb.mp3",
    67: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122149_1342e610-3ef0-4f84-9626-5a2f13b763ca.mp3",
    68: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122149_d341fb04-51ce-439b-bdff-9d0b60bd29ad.mp3",
    69: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122150_7fb12a96-1ad2-42bc-83a3-b546b0ea4fbb.mp3",
    70: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_122407_46ed88ec-660a-4c18-b670-779723af2b92.mp3",
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
