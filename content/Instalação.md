Title: Primeiros Passos
Date: 2016-02-07 15:14
Category: 1 - Instalação

## Enthought Canopy

O ambiente de desenvolvimento das rotinas apresentadas neste site será o **Enthought Canopy**. Este software facilita em muito a aprendizagem por ser mais *user friendly*, possuir atalhos de teclado bem úteis e facilitar a instalação de alguns pacotes, como o **NetCDF4**. 

## Licença

Este software é gratuito para uso acadêmico, então, para baixá-lo é preciso primeiro [criar uma conta][], informando que instituição acadêmica você está vinculado e utilizar seu email acadêmico. 
Alguns emails acadêmicos, como o @usp.br, são automaticamente vinculados a uma licença acadêmica, se este não for o seu caso, talvez tenha que esperar alguns dias para a validação.

## Download

Após a validação você fará login e então, clicando em **Account** no canto superior direito da tela:
![Passo 1](/images/canopy_install0.png){: style='width: 400px; height: auto}

Depois vá na seção Downloads:

![Passo 2](/images/canopy_install1.png){: style='width: 400px; height: auto}

E clique para baixar o Canopy:

![Passo 3](/images/canopy_install2.png){: style='width: 600px; height: auto'}


## Instalação do Canopy

Uma das formas de organizar os programas instalados no Linux é criar uma pasta em sua */home* para abrigar os programas e seus instaladores, evitando que sua */home* se encha de diretórios.

      mkdir /home/username/Programs/Enthought/Canopy
      
Este comando criará tanto o diretório Programs como também o diretório Enthought, onde será instalado o Canopy. Agora copie o o instalador do Canopy para a pasta Enthought, acesse-a com o terminal e rode:

      bash canopy-1.6.2-rh5-64.sh

O nome do instalador pode variar com a versão ou máquina que você estiver usando.
Aceite os termos e então escreva o caminho para o diretório Canopy criado no comando anterior:

![Passo 4](/images/canopy_install3.png){: style='width: 600px; height: auto'}

Após a instalação, abra o Canopy:

![Passo 5](/images/canopy_install4.png){: style='width: 600px; height: auto'}

Aceite que o Canopy seja o *Default* do sistema operacional para abrir arquivos em python e logue-se com sua conta acadêmica:

![Passo 6](/images/canopy_install5.png){: style='width: 600px; height: auto'}

Agora precisamos ativar o **pip** para instalar pacotes no Canopy. O **pip** é um repositório de pacotes em *Python*. Para isso execute os seguintes comandos no terminal:

      enpkg setuptools
      enpkg pip

## Instalação dos módulos necessários

Agora que temos o Canopy instalado precisamos instalar os módulos em python que serão utilizados nos tutoriais. Para isso, abra o Canopy a pasta e acesse o *Package Manager*. Dentro deste, certifique-se que está logado e então procure por *netcdf*:

Instale todos os pacotes assinalados:

![Passo 7](/images/canopy_install7.png){: style='width: 600px; height: auto'}

Crtifique-se que todos estão com o selo verde:

![Passo 8](/images/canopy_install8.png){: style='width: 600px; height: auto'}

Agora procure por *basemap* e instale os dois pacotes que aparecem:

![Passo 9](/images/canopy_install9.png){: style='width: 600px; height: auto'}

Agora acesse a pasta */Programs* em seu */home* e execute o seguinte comando para baixar os módulos OceanLab:

      git clone https://github.com/iuryt/OceanLab.git
      cd OceanLab/

Agora execute o seguinte comando para instalar os módulos:

      python setup.py install
      
## Certificando-se que tudo foi instalado

Abra o *Editor* do Canopy, vá para a janela que tenha escrito *"Welcome to Canopy's interactive data-analysis environment!
"* e execute os seguintes comandos:

      from OceanLab import *
      from mpl_toolkits.basemap import Basemap
      import pandas
      import numpy
      import scipy
      import matplotlib

Se não ocorrer nenhum erro é porque foi tudo instalado corretamente.

![Passo 10](/images/canopy_install10.png){: style='width: 600px; height: auto'}     

[Enthought Canopy]: https://www.enthought.com/products/canopy/
[criar uma conta]: https://store.enthought.com/accounts/login/
