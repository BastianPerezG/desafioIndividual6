from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class FormularioUsuarios(forms.Form):
    rut = forms.CharField               (label="Rut", required = True, max_length=12,
                                        error_messages={
                                            'required': 'Ingrese el RUT del usuario',
                                            'max_length': 'El RUT no puede tener más de 12 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'Ingrese su Rut',
                                            'class':'form-control'})
                                        )
    nombreUsuario = forms.CharField  (label="NombreUsuario", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El nombre de usuario es obligatorio',
                                            'max_length': 'El nombre debe tener como maximo 10 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre de usuario',
                                            'class':'form-control'}),
                                        )
    nombre = forms.CharField            (label="Nombre", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El nombre del usuario es Obligatorio',
                                            'max_length': 'El nombre debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del usuario',
                                            'class':'form-control'}),
                                        )

    apellido = forms.CharField          (label="Apellido", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El apellido del usuario es obligatorio',
                                            'max_length': 'El apellido debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el apellido del usuario',
                                            'class':'form-control'}),
                                        )
    email = forms.EmailField            (label="Email", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el email del usuario',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'Ingrese su correo electrónico',
                                            'class':'form-control',
                                            'type':'email'})
                                        )
    
class FormularioLogin(forms.Form):
    username = forms.CharField(label='NombreUsuario', required=True,
                                max_length=30, min_length=5,
                                error_messages={
                                    'required': 'El nombre de usuario es obligatorio',
                                    'max_length': 'El usuario no puede superar los 30 caracteres',
                                    'min_length': 'El usuario debe tener al menos 5 caracteres'
                                },
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Ingrese su nombre de usuario',
                                    'class': 'form-control'
                                })
                                )
    password = forms.CharField(label='Contraseña', required=True,
                                max_length=30, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 30 caracteres',
                                    'min_length': 'La contraseña debe tener al menos 1 caracter'
                                },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )
    
class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label='NombreUsuario', required=True,
                                max_length=30, min_length=5,
                                error_messages={
                                    'required': 'El nombre de usuario es obligatorio',
                                    'max_length': 'El usuario no puede superar los 30 caracteres',
                                    'min_length': 'El usuario debe tener al menos 5 caracteres'
                                },
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Ingrese su nombre de usuario',
                                    'class': 'form-control'
                                })
                                )
    first_name = forms.CharField            (label="Nombre", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El nombre del usuario es Obligatorio',
                                            'max_length': 'El nombre debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del usuario',
                                            'class':'form-control'}),
                                        )

    last_name = forms.CharField          (label="Apellido", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El apellido del usuario es obligatorio',
                                            'max_length': 'El apellido debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el apellido del usuario',
                                            'class':'form-control'}),
                                        )
    email = forms.EmailField    (label="Email", required = True, max_length=30,
                                    error_messages={
                                            'required': 'Tiene que indicar el email del usuario',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                    widget= forms.TextInput(attrs={
                                            'placeholder':'Ingrese su correo electrónico',
                                            'class':'form-control',
                                            'type':'email'})
                                    )
    image = forms.ImageField(label='Foto de perfil', required=False,
                            error_messages={
                                            'max_weigth': 'El peso de la imagen no debe superar los 50mb',
                                        })
                            
                                    
    password1 = forms.CharField(label='Contraseña', required=True,
                                max_length=30, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 30 caracteres'
                                    },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )
    password2 = forms.CharField(label='Contraseña', required=True,
                                max_length=30, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 30 caracteres'
                                    },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

    def ruta_fotoPerfil(self):
        return 'static/assets/img/foto_perfil.png'
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name','email','image', 'password1', 'password2', 'group')
