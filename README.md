# Insta Unfollower Checker

A simple Python script that compares your Instagram follower list with your following list to identify who unfollowed you.

---

## What it Does

This script takes your Instagram followers and following lists (exported from Instagram as JSON files) and compares them. It then outputs which accounts you follow that are **not following you back** — effectively showing who unfollowed you.

---

## How to Use

1. **Download your Instagram data:**  
   Go to Instagram settings and request your data download. Once you receive it, locate the JSON files containing your **followers** and **following** lists.

2. **Prepare your files:**  
   Place the `followers.json` and `following.json` files in the same directory as the script, or provide the relative or absolute path to the files when running the script.

3. **Run the script:**  
   Use the command line to run the script with Python, providing the followers file first, then the following file. For example:

   ```bash
   python insta_followers.py followers.json following.json

If your files are in a different directory then:
```bash
python insta_followers.py path/to/followers.json path/to/following.json
```

## How It Works

- The script uses a hash map (dictionary) for constant time O(1) lookups to efficiently compare the two lists.

- It identifies users you follow who do not follow you back, letting you know who unfollowed you.

## Requirements
- Python 3.x

## Download
To download run the following command:
```bash
git clone https://github.com/Xuxuh15/InstaExiters.git
```

