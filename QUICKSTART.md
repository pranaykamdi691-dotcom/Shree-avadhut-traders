# Quick Start - Copy Paste Commands

## Windows Users (सिर्फ Copy-Paste करो)

### Command 1: Clone करें
```
git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
cd Shree-avadhut-traders
```

### Command 2: Virtual Environment बनाएं
```
python -m venv venv
venv\Scripts\activate
```

### Command 3: Dependencies Install करें
```
pip install --upgrade pip
pip install -r requirements.txt
```

### Command 4: .env File Copy करें
```
copy .env.example .env
```

### Command 5: App चलाएं
```
python run.py
```

✅ Browser खोलो: **http://localhost:5000**

---

## Mac/Linux Users (सिर्फ Copy-Paste करो)

### Command 1: Clone करें
```
git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
cd Shree-avadhut-traders
```

### Command 2: Virtual Environment बनाएं
```
python3 -m venv venv
source venv/bin/activate
```

### Command 3: Dependencies Install करें
```
pip install --upgrade pip
pip install -r requirements.txt
```

### Command 4: .env File Copy करें
```
cp .env.example .env
```

### Command 5: App चलाएं
```
python run.py
```

✅ Browser खोलो: **http://localhost:5000**

---

## 🎯 First Time Login

1. Home page पर "Register" बटन दिखेगा
2. ये information भरो:
   - **Username:** कोई भी नाम (जैसे: john_doe)
   - **Email:** तुम्हारा email (जैसे: john@gmail.com)
   - **Password:** कोई strong password (कम से कम 8 characters)
   - **Company Name:** तुम्हारी company (जैसे: Shree Avadhut Traders)
   - **GSTIN:** GST number (optional - बाद में भर सकते हो)

3. "Register" बटन दबाओ
4. Login करो अपने username और password से

---

## 📱 Dashboard में क्या-क्या कर सकते हो?

### 1. Customers Add करना
- "Customers" मेनू पर जाओ
- "Add New Customer" बटन दबाओ
- Customer details भरो
- Save करो

### 2. Invoice Create करना
- "Invoices" मेनू पर जाओ
- "Create Invoice" बटन दबाओ
- Customer select करो
- Items add करो
- GST automatically calculate होगा
- Invoice save करो

### 3. Reports देखना
- "Reports" मेनू पर जाओ
- Date range select करो (optional)
- GST summary देखो
- PDF download करो

---

## ❓ Common Problems और Solutions

### Problem 1: "git command not found"
**Solution:** Git install करो from https://git-scm.com/

### Problem 2: "python not found"
**Solution:** Python install करो from https://www.python.org/downloads/

### Problem 3: Port 5000 already in use
**Solution:** 
```
python run.py --port 5001
```
फिर browser में खोलो: http://localhost:5001

### Problem 4: Module not found error
**Solution:** Virtual environment activate है या नहीं check करो
```
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Problem 5: Database error
**Solution:** Database delete करो और restart करो
```
rm gst_app.db
python run.py
```

---

## 🛑 App को Stop करना

Terminal में **Ctrl + C** दबाओ

---

## 🔄 App को फिर से चलाना

```
# Terminal खोलो
cd Shree-avadhut-traders
venv\Scripts\activate        (Windows के लिए)
source venv/bin/activate     (Mac/Linux के लिए)
python run.py
```

---

## 📞 Support

अगर कोई problem आए तो:
1. INSTALL.md file पढ़ो
2. TROUBLESHOOTING section check करो
3. GitHub issue create करो

---

## ✨ अब आप GST App use कर सकते हो! 🎉

Happy coding! 😊
